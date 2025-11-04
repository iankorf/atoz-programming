# beat_box.py

import time

target = 4
while True:
	print(f'Get ready to hit the enter key exactly {target} seconds apart!')
	input('Press enter when ready...')
	t0 = time.time()
	input(f'Press the enter key after exactly {target} seconds! ')
	t1 = time.time()
	elapsed = t1 - t0
	off = abs(target - elapsed)
	print(f'Your time: {elapsed} was off by {100*off/target:.2f} percent.')
