"""
QUESTION:
For a given positive integer M, calculate the sum T(M) of N(u^3/v^3) where (u,v) spans over all ordered pairs of mutually prime positive integers not exceeding M, and N(r) is the least positive integer n such that s(n) = r*n, where s(n) is the integer derived by translocating the leftmost digit of the decimal representation of n to the rightmost position. If no such integer is found, then N(r) is defined as zero. Return T(M) modulo 1,000,000,007.

Implement a function T(M) that calculates this sum.
"""

MODULUS = 10**9+7

def coprime(a, b):
    while b != 0:
        a, b = b, a % b
    return a == 1

def solve(x):
    L = 10**(len(str(x))-1)
    n = (10*x+1)//18
    if (10*n - n//10)*9 != x*n:
        n -= 1
    while True:
        n1 = n//L*10
        n2 = n - n1*L
        if n2 < (n1%10)*L//10: n1 -= 1
        n = min(n, n1*L+L-1)
        if (10*n - n//10)*9 == x*n:
            return n % MODULUS
        n -= 1

def entrance(M):
    result = 0
    for v in range(1, M+1):
        result += solve(v*v*v)
        for u in range(1, v):
            if coprime(u, v):
                result += solve(u*u*u*v*v)
    return result % MODULUS