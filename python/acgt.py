# acgt.py

import random

r = random.random()
if r > 0.3:
	print('A')
elif r > 0.5:
	print('C')
elif r > 0.7:
	print('G')
else:
	print('T')
