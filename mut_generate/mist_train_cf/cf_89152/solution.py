"""
QUESTION:
Implement a function `gcd(A, B)` that calculates the greatest common divisor of two positive integers `A` and `B`, where 1 <= A, B <= 10^9, without using any built-in GCD functions, libraries, or division-related operators. The function should have a time complexity of O(log(min(A,B))) or better.
"""

def gcd(A, B):
    if A == 0:
        return B
    elif B == 0:
        return A
    elif A == B:
        return A
    elif A == 1 or B == 1:
        return 1
    
    if A > B:
        smaller = B
        larger = A
    else:
        smaller = A
        larger = B
    
    while smaller != 0:
        temp = smaller
        smaller = larger % smaller
        larger = temp
    
    return larger