"""
QUESTION:
Create a function `lcm` that takes two integers `x` and `y` as input, where `x` is not divisible by 2 and `y` is not divisible by 3, and returns their Least Common Multiple (LCM) if it is greater than 1000 and the sum of its digits is a prime number.
"""

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def gcd(x, y):
    """Calculate the Greatest Common Divisor of two numbers."""
    while(y):
        x, y = y, x % y
    return x

def lcm(x, y):
    """Calculate the Least Common Multiple of two numbers if the first number is not divisible by 2 and the second number is not divisible by 3, and return it if it's greater than 1000 and the sum of its digits is a prime number."""
    if x % 2 == 0 or y % 3 == 0:
        return None
    lcm_value = (x * y) // gcd(x, y)
    if lcm_value > 1000 and is_prime(sum(int(digit) for digit in str(lcm_value))):
        return lcm_value
    return None