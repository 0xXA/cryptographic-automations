#!/usr/bin/env python

# Trial Division Method

from typing import List
from math import sqrt

def tdm(n: int) -> List[int]:
	result = []
	a = 2
	while a <= sqrt(n):
		while (n%a) == 0:
			result.append(a)
			n = n / a
		a = a + 1
	if n > 1:
		if isinstance(n,float): # type(n) == float
			n = int(n)
		result.append(n)
	return result

print(tdm(int(input('Enter a number to factorize: '))))