# Pi = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) -4/(8*9*10) ...
#Pi/4 = 1/1 - 1/3 + 1/5 - 1/7 + 1/9 ...

# Gregory-Leibniz odd-even

pi4 = 0
for i in range(1000):
	if i % 2 == 0: pi4 += 1/(1 + i*2)
	else:          pi4 -= 1/(1 + i*2)
print('Gregory odd-even:', pi4*4)

# Gregory-Leibniz flip-flop -1

pi4 = 0
sign = 1
for i in range(1, 2000, 2):
	pi4 += 1/i * sign
	sign *= -1
print('Gregory flip-flop:', pi4 * 4)

# Nilakantha Boolean (definite loop)

pi = 3
plus = True
for i in range(2, 20, 2):
	d = i * (i+1) * (i+2)
	if plus: pi = pi + 4/d
	else:    pi = pi - 4/d
	plus = not plus
print('Nilakantha definite:', pi)

# Nilakantha end on precision (indefinite loop)

pi = 3
i = 2
prev = 0
sign = 1
while abs(pi - prev) > 1e-3:
	prev = pi
	d = i * (i+1) * (i+2)
	pi = pi + (sign * 4/d)
	sign = sign * -1
	i += 2
	print('Nilakantha indefinite:', pi)

# Random darts infinite loop

import random
import math

inside = 1
outside = 1
while True:
	x = random.random()
	y = random.random()
	d = math.sqrt(x**2 + y**2)
	if d > 1: outside += 1
	else:     inside  += 1
	print('Infinite:', 4 * inside / (inside + outside))
