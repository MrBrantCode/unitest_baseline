"""
QUESTION:
Write a recursive function called `print_prime_cubes(n)` that takes an integer `n` as input and prints the cube of numbers from `n` down to 1, but only if the cubed number is a prime number.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_prime_cubes(n):
    if n > 0:
        cube = n**3
        if is_prime(cube):
            print(cube)
        print_prime_cubes(n-1)