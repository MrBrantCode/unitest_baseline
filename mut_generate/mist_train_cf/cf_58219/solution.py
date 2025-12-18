"""
QUESTION:
Create a function named `prime_or_composite` that takes an integer `num` as input and returns 'Prime Number' if the number is prime, or a list of factors if the number is composite. The function should use the modulus operator to check for primality and only check up to the square root of the number for efficiency.
"""

def prime_or_composite(num):
    if num > 1 and all(num % i for i in range(2, int(num ** 0.5) + 1)) > 0:
        return 'Prime Number'
    else:
        return [i for i in range(1, num + 1) if num % i == 0]