"""
QUESTION:
Implement the `myPow` function in Python, which calculates the power of a given base number. The function takes two parameters: `x` (float) as the base number and `n` (int) as the power number. The function should return the result of raising the base number `x` to the power of `n`.
"""

def myPow(x, n):
    if n == 0:
        return 1
    if n < 0:
        x = 1 / x
        n = -n
    result = 1
    while n > 0:
        if n % 2 == 1:
            result *= x
        x *= x
        n //= 2
    return result