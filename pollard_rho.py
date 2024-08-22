from math import gcd
from random import randint

def pollard_rho(n):
    x1 = 2
    x2 = x1
    p = 1

    while p == 1:
        x1 = (pow(x1,2)+1)%n
        x2 = (pow(x2,2)+1)%n
        x2 = (pow(x2,2)+1)%n
        p = gcd(abs(x1-x2),n)

    if p == n:
        # Failure
        return -1
    else:
        return p

def pollard_rho_optimized(n, nRetry=0, mRetry=5):
    x1 = 2
    x2 = x1
    p = 1
    a = randint(0, 1)

    if n == 1:
        return 1
    
    if n % 2 == 0:
        return 2

    while p == 1:
        x1 = (pow(x1,2)+a)%n
        x2 = (pow(x2,2)+a)%n
        x2 = (pow(x2,2)+a)%n
        p = gcd(abs(x1-x2),n)
        # If we fail for the very first time, then retry for atmost mRetry number of times before failing.
        if p == n and nRetry < mRetry:
            nRetry += 1
            return pollard_rho_optimized(n, nRetry, mRetry)

    if p == n:
        # Failure
        return -1
    else:
        return p
    
print(f'Normal: {[pollard_rho(25) for x in range(100)]}')
print(f'Optimized: {[pollard_rho_optimized(25,0,100) for x in range(100)]}') # With more tries we increase the chances of success.