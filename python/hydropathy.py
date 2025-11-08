import sys

seq = sys.argv[1]

# using if-elif-else
kd = 0
for aa in seq:
	if   aa == 'I': kd +=  4.5
	elif aa == 'V': kd +=  4.2
	elif aa == 'L': kd +=  3.8
	elif aa == 'F': kd +=  2.8
	elif aa == 'C': kd +=  2.5
	elif aa == 'M': kd +=  1.9
	elif aa == 'A': kd +=  1.8
	elif aa == 'G': kd += -0.4
	elif aa == 'T': kd += -0.7
	elif aa == 'S': kd += -0.8
	elif aa == 'W': kd += -0.9
	elif aa == 'Y': kd += -1.3
	elif aa == 'P': kd += -1.6
	elif aa == 'H': kd += -3.2
	elif aa == 'E': kd += -3.5
	elif aa == 'Q': kd += -3.5
	elif aa == 'D': kd += -3.5
	elif aa == 'N': kd += -3.5
	elif aa == 'K': kd += -3.9
	elif aa == 'R': kd += -4.5
	else: sys.exit(f'ERROR: unknown amino acid {aa}')
print(f'Average hydropathy: {kd / len(seq):.3f}')

# using match-case
kd = 0
for aa in seq:
	match aa:
		case 'I': kd +=  4.5
		case 'V': kd +=  4.2
		case 'L': kd +=  3.8
		case 'F': kd +=  2.8
		case 'C': kd +=  2.5
		case 'M': kd +=  1.9
		case 'A': kd +=  1.8
		case 'G': kd += -0.4
		case 'T': kd += -0.7
		case 'S': kd += -0.8
		case 'W': kd += -0.9
		case 'Y': kd += -1.3
		case 'P': kd += -1.6
		case 'H': kd += -3.2
		case 'E': kd += -3.5
		case 'Q': kd += -3.5
		case 'D': kd += -3.5
		case 'N': kd += -3.5
		case 'K': kd += -3.9
		case 'R': kd += -4.5
		case _:   sys.exit(f'ERROR: unknown amino acid {aa}')
print(f'Average hydropathy: {kd / len(seq):.3f}')

# using parallel containers (string, list)
aas = 'IVLFCMAGTSWYPHEQDNKR'
kds = [4.5, 4.2, 3.8, 2.8, 2.5, 1.9, 1.8, 0.4, -0.7, -0.8, -0.9, -1.3, -1.6,
	-3.2, -3.5, -3.5, -3.5, -3.5, -3.9, -4.5]
kd = 0
for aa in seq:
	pos = aas.find(aa) # could also use aas.index(aa)
	if pos == -1: sys.exit(f'ERROR: unknown amino acid {aa}')
	kd += kds[pos]
print(f'Average hydropathy: {kd / len(seq):.3f}')
