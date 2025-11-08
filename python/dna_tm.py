# oligo tm

# tm1() uses a "for" loop to count the letters
def tm1(oligo):
	a = 0
	c = 0
	g = 0
	t = 0
	for nt in oligo:
		if   nt == 'A': a += 1
		elif nt == 'C': c += 1
		elif nt == 'G': g += 1
		elif nt == 'T': t += 1
		else: raise Exception('ERROR: only A, C, G, T allowed')
	if a + c + g + t <= 13:
		return (a+t)*2 + (c+g)*4
	else:
		return 64.9 + 41 * (c+g -16.4) / (a+c+g+t)

# tm2() uses "str.count()" to count the letters
def tm2(oligo):
	a = seq.count('A')
	c = seq.count('C')
	g = seq.count('G')
	t = seq.count('T')
	if a + c + g + t < len(seq):
		raise Exception('ERROR: only A, C, G, T allowed')
	if a + c + g + t <= 13:
		return (a+t)*2 + (c+g)*4
	else:
		return 64.9 + 41 * (c+g -16.4) / (a+c+g+t)

while True:
	seq = input('Oligo sequence: ')
	if len(seq) == 0: break
	seq = seq.upper()
	t = tm1(seq)
	print(f'The Tm of {seq} is {t:.3f}C')

