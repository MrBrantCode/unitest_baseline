"""
QUESTION:
Create a function named `create_cube_dictionary` that takes an integer `n` as input. This function should generate a dictionary where each key is a number from 0 to `n-1`, and its corresponding value is the cube of the key, but only if the key is a prime number. Additionally, the function should return the total count of prime numbers added to the dictionary. The primality test must be implemented as a separate function named `is_prime`. Do not use any external libraries for primality testing.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def create_cube_dictionary(n):
    cube_dict = {}
    prime_count = 0
    for num in range(n):
        if is_prime(num):
            cube_dict[num] = num ** 3
            prime_count += 1
    return cube_dict, prime_count