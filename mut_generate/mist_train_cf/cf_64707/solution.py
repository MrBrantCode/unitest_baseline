"""
QUESTION:
Create a function `is_prime(n)` to check if a given integer `n` is a prime number. Using this function, create a tuple `my_tuple` with exactly five prime numbers under 50 and verify that all numbers in the tuple are indeed prime. The prime numbers for the tuple should be manually selected, without using any pre-defined list or module. In this task, 1 is not considered a prime number.
"""

def is_prime(n):
    """Check if integer n is a prime"""
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True