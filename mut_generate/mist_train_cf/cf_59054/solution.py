"""
QUESTION:
Write a function `prime_generator` that generates and returns all prime numbers within the range of 1000 to 1500 (inclusive). The function should not take any parameters.
"""

def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))

def prime_generator():
    return [number for number in range(1000, 1501) if is_prime(number)]