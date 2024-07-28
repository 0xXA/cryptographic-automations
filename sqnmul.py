#!/usr/bin/env python

# Square and Multiply Algorithm to calculate exponent of a number in the destination set Z_{n}.

# y = a^x mod n
def sqnmul(a : int, x : int, n : int) -> int:
	y = 1
	a = a % n

	while x > 0:
		if x & 1:
			y = (a*y)%n
		x >>= 1
		a = (a*a)%n
	return y

for x in range(1,16):
	print(sqnmul(84848493939393333393333333338484848, x, 1500838381838183838383838388338838300000))