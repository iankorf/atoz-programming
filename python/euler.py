# euler.py

import math

e = 0
n = 0
prev = 0
while True:
	e += 1 / math.factorial(n)
	if e == prev: break
	prev = e
	n += 1
	print(e)
