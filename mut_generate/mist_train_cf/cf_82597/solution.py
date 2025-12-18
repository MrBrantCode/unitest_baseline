"""
QUESTION:
Implement a function `lcm` that takes two integers as input and returns their Least Common Multiple (LCM) using the Euclidean algorithm. The LCM should be calculated as the product of the two numbers divided by their Greatest Common Divisor (GCD).
"""

def lcm(primeFactorX, primeFactorY):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    lcm = (primeFactorX * primeFactorY) // gcd(primeFactorX, primeFactorY)
    return lcm