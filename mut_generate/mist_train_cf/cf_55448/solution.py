"""
QUESTION:
Implement a function named `karatsuba(x, y)` that multiplies two integers `x` and `y` using the Karatsuba algorithm. The function should be able to handle integers of any length. It should not use the built-in multiplication operator (`*`) for numbers with 10 or more digits, instead relying on recursive calls to itself to break down the multiplication into smaller sub-problems.
"""

def karatsuba(x, y):
    # Base case:
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    n //= 2

    a = x // 10**(n)
    b = x % 10**(n)
    c = y // 10**(n)
    d = y % 10**(n)

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_plus_bc = karatsuba(a + b, c + d) - ac - bd

    return ac * 10**(2 * n) + (ad_plus_bc * 10**n) + bd