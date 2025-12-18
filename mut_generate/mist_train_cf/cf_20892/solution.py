"""
QUESTION:
Write a function `remove_largest_prime` that takes a list of integers as input and returns the modified list after deleting all occurrences of the largest prime number.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def remove_largest_prime(numbers):
    largest_prime = max([num for num in numbers if is_prime(num)], default=None)
    return [num for num in numbers if num != largest_prime]