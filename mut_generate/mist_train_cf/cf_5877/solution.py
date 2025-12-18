"""
QUESTION:
Implement a function `gcd(A, B)` to calculate the greatest common divisor of two positive integers `A` and `B` where 1 <= `A`, `B` <= 10^9 without using any built-in GCD functions, libraries, modulus operator, or division-related operators, and achieve a time complexity of O(log(min(A,B))) or better.
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
    
    # Finding the smaller number between A and B
    if A > B:
        smaller = B
        larger = A
    else:
        smaller = A
        larger = B
    
    # Iteratively finding the GCD
    while smaller != 0:
        temp = smaller
        smaller = larger - (larger // smaller) * smaller
        larger = temp
    
    return larger