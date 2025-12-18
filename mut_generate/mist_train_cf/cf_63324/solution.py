"""
QUESTION:
Create a dictionary, `prime_cube`, where the keys are prime numbers within the range 1 to 50 (inclusive) and their corresponding values are the cubes of these prime numbers. You are required to implement a helper function, `is_prime(n)`, to check if a number `n` is prime. The `prime_cube` dictionary should be generated using a dictionary comprehension.
"""

def is_prime(n):
    if n < 2:
       return False
    for i in range(2, int(n**(0.5)) + 1):
       if n % i == 0:
           return False
    return True

def prime_cube_dict():
    return {num: num**3 for num in range(1, 51) if is_prime(num)}