"""
QUESTION:
Implement a function `calculateF(N)` that calculates the value of `F(N)`, where `F(N) = sum(n/d(n)) from n=1 to N`, `d(n)` is the sum of the digits of `n`, and `N` is a positive integer. The result should be expressed in scientific notation with a precision of up to twelve significant digits following the decimal point, using a lowercase 'e' to separate the mantissa and exponent. The function should be able to handle very large values of `N`.
"""

def calculateF(N):
    def d(n):
        return sum(int(digit) for digit in str(n))
    return sum(n/d(n) for n in range(1, N + 1))