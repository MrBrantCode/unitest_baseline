"""
QUESTION:
Create a function named LCM3Nums that takes three integers a, b, and c as input and returns their least common multiple (LCM) without using any built-in Python functions for GCD or LCM calculations. The function should be efficient and optimized. You can use a helper function if necessary.
"""

def LCM3Nums(a, b, c):
    def GCD(x, y):
        if y > x:
            return GCD(y, x)
        elif x % y == 0:
            return y
        else:
            return GCD(y, x % y)

    def LCM2Nums(x, y):
        return x * y // GCD(x, y)

    return LCM2Nums(LCM2Nums(a, b), c)