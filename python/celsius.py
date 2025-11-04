# celsius.py

while True:
	ans = input('What temperature to convert (e.g. 37C or 98.6F): ')
	if len(ans) == 0: break
	temp1 = float(ans[:-1])
	scale1 = ans[-1]
	if scale1 == 'F':
		temp2 = (temp1 - 32) * 5 / 9
		scale2 = 'C'
	else:
		temp2 = temp1 * 9 / 5 + 32
		scale2 = 'F'
	print(f'{temp1}{scale1} is {temp2}{scale2}')
