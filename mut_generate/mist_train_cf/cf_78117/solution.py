"""
QUESTION:
Write a function named `solve` that takes three integers `a`, `b`, and `c` as input, subtracts `b` from `a` to find the difference, and then calculates the least common multiple of the difference and `c`. The function should return the least common multiple.
"""

def solve(a, b, c):
    def gcd(x, y):
        while(y):
            x, y = y, x % y
        return x

    def lcm(x, y):
        lcm = (x * y) // gcd(x, y)
        return lcm

    difference = a - b
    result = lcm(difference, c)
    return result