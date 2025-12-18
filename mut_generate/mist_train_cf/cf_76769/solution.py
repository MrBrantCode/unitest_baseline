"""
QUESTION:
Create a function named `is_prime` that takes an integer `n` as input. The function should return `True` if `n` is a prime number and `False` otherwise. The prime number check should be implemented without using any built-in or external libraries. The function should then be used in a loop that iterates over a given numerical array to print the index and value of each prime number in the array.
"""

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        sqrtn = int(n**0.5)+1
        for divisor in range(3, sqrtn, 2):
            if n % divisor == 0:
                return False
        return True