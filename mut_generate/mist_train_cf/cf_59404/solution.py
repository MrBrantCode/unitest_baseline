"""
QUESTION:
Implement a function `karatsuba(num1, num2)` that takes two integers as input and returns their product using the Karatsuba multiplication algorithm. The function should handle numbers of any size, but for simplicity, assume that the input numbers are non-negative.
"""

def karatsuba(num1, num2):
    if num1 < 10 or num2 < 10:
        return num1*num2

    n1 = len(str(num1))
    n2 = len(str(num2))

    N = max(n1,n2)
    N -= N & 1

    a, b = divmod(num1, 10**(N//2))
    c, d = divmod(num2, 10**(N//2))

    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    ad_plus_bc = karatsuba(a+b,c+d) - ac - bd

    return (((10**N)*ac) + bd + ((10**(N//2))*(ad_plus_bc)))