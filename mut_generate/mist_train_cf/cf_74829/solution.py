"""
QUESTION:
Create a function `is_prime` that takes an integer `n` as input and returns a boolean indicating whether `n` is a prime number. Use this function to generate and print a list of all prime numbers between 1 and 100. The function should be efficient and handle large inputs by minimizing the number of divisions performed.
"""

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n%2 == 0 or n%3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n%i == 0 or n%(i+2) == 0:
            return False
        i += 6
    return True