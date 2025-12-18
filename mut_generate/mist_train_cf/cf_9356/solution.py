"""
QUESTION:
Write a function `calculate_lcm` that takes two integers `x` and `y` as input, where `x` is not divisible by 2 and `y` is not divisible by 3. The function should return the Least Common Multiple (LCM) of `x` and `y`, but only if the LCM is greater than 100.
"""

def calculate_lcm(x, y):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    lcm = (x * y) // gcd(x, y)
    return lcm if lcm > 100 else None