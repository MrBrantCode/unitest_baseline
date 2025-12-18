"""
QUESTION:
Implement a recursive function `lcm_three(a, b, c)` to calculate the least common multiple (LCM) of three numbers `a`, `b`, and `c` without using any predefined Python functions like `gcd()` or `math.gcd()`. Note that you will need to implement a helper function `gcd(a, b)` to calculate the greatest common divisor of two numbers using the Euclidean algorithm. The function `lcm_three(a, b, c)` should return an integer result.
"""

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm_two(a, b):
    return (a * b) // gcd(a, b)

def lcm_three(a, b, c):
    return lcm_two(a, lcm_two(b, c))