"""
QUESTION:
Define n!! as

n!! = 1 \* 3 \* 5 \* ... \* n  if n is odd, 

n!! = 2 \* 4 \* 6 \* ... \* n  if n is even. 

Hence 8!! = 2 \* 4 \* 6 \* 8 = 384, there is no zero at the end. 
30!! has 3 zeros at the end. 

For a positive integer n, please count how many zeros are there at 
the end of n!!. 

Example: 

count\_zeros\_n\_double\_fact(30) should return 3
"""

def count_trailing_zeros_in_double_factorial(n):
    if n % 2 != 0:
        return 0
    k = 0
    while n >= 10:
        k += n // 10
        n //= 5
    return k