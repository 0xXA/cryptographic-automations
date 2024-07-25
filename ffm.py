#!/usr/bin/env python

# Fermat's Factorization Method

from typing import List
from math import sqrt, floor, ceil

def isperfect(n):
	a = int(sqrt(n))
	if a*a == n:
		return True
	else:
		return False

def ffm(n: int) -> List[[int, int]]:
	result = []
	x = ceil(sqrt(n))
	while x < n:
		w = x*x - n
		if isperfect(w):
			y = int(sqrt(w))
			a = x + y
			b = x - y
			result.append([a,b])
			# Uncomment below line if all factors are not required
			# return result
		x = x + 1
	return result

print(ffm(int(input('Enter a number to factorize: '))))