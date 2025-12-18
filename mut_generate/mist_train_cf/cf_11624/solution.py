"""
QUESTION:
Generate a function called `generate_prime_array` that creates a 2D array with unique prime numbers. The function should take two parameters: `rows` and `cols`, representing the dimensions of the array. The function should return a 2D array where each element is a unique prime number, and the array has the specified number of rows and columns.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime_array(rows, cols):
    primes = []
    num = 2
    while len(primes) < rows * cols:
        if is_prime(num):
            primes.append(num)
        num += 1
    return [primes[i * cols:(i + 1) * cols] for i in range(rows)]