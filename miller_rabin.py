#!/usr/bin/env python

# Miller Rabin Test to check if a number is composite or not
# It's a type Randomized Algorithm commonly known as a "yes"-biased Monte Carlo Algorithm.

from math import pow
from random import randint

def sqnmul(a : int, x : int, n : int) -> int:
	y = 1
	a = a % n

	while x > 0:
		if x & 1:
			y = (a*y)%n
		x = x >> 1
		a = (a*a)%n
	return y

def iscomposite(n : int) -> bool:
	tmp = 1
	m = 1
	k = 1

	while True:
		tmp = (n-1) / pow(2,k)
		# Extract the fractional part
		frpart = int((tmp % 1)*100)
		if frpart == 0 and int(tmp) & 1: # if the fractional part is zero and is odd, capture it
			m = int(tmp)
		if frpart > 0:
			break
		k = k + 1

	a = randint(1, n-1)
	b = sqnmul(a, m, n)

	if (b%n) == 1:
		return False

	for i in range(k):
		if (b%n) == -1:
			return False
		else:
			b = (b*b)%n
	return True

x = int(input('Enter a number to check for primality: '))

if not iscomposite(x):
	print('Yes!',x,'is a prime number')
else:
	print('No!',x,'is not a prime number')
