"""
QUESTION:
Create a function named `lcm_three_numbers` that takes three positive integers `a`, `b`, and `c` as input and returns their least common multiple (LCM). The function should not accept non-integer or non-positive inputs. The solution should utilize the formula LCM(a, b, c) = LCM(LCM(a, b), c) and calculate the LCM using the greatest common divisor (GCD).
"""

def lcm_three_numbers(a, b, c):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return (a * b) // gcd(a, b)

    return lcm(lcm(a, b), c)