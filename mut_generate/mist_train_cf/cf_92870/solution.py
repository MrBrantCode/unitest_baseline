"""
QUESTION:
Write a function `lcm_three_numbers` that takes three positive integers `a`, `b`, and `c` as input and returns their least common multiple.
"""

def lcm_three_numbers(a, b, c):
    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x

    def lcm(x, y):
        return (x * y) // gcd(x, y)

    return lcm(lcm(a, b), c)