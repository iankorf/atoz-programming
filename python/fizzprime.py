# fizzprime.py

import math

def is_prime(n):
	if n == 1: return False
	for i in range(2, n):
		if n % i == 0: return False
	return True

def is_prime_odd(n):
	if n == 1: return False
	if n == 2: return True
	if n % 2 == 0: return False
	for i in range(3, n // 2, 2):
		if n % i == 0: return False
	return True

def is_prime_root(n):
	if n == 1: return False
	if n == 2: return True
	if n % 2 == 0: return False
	for i in range(3, 1+int(math.sqrt(n))):
		if n % i == 0: return False
	return True

for i in range(1, 101):
	if   i % 15 == 0: print('FizzBuzz', end='')
	elif i %  5 == 0: print('Buzz', end='')
	elif i %  3 == 0: print('Fizz', end='')
	else:             print(i, end='')

	if is_prime(i): print('*')
	else:           print()

"""
# alternate printing using f-strings
for i in range(1, 101):
	star = '*' if is_prime(i) else ''
	if   i % 15 == 0: print(f'FizzBuzz{star}')
	elif i %  5 == 0: print(f'Buzz{star}')
	elif i %  3 == 0: print(f'Fizz{star}')
	else:             print(f'{i}{star}')

"""
