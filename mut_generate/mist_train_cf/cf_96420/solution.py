"""
QUESTION:
Write a function named `find_second_highest_prime` that takes a list of integers as input, finds the second highest prime number in the list, and returns it. If the list is empty or contains less than two prime numbers, raise an exception with a corresponding error message. Assume that the input list contains only positive integers.
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_second_highest_prime(numbers):
    primes = [num for num in numbers if is_prime(num)]
    if len(primes) < 2:
        raise Exception("Error: Less than two prime numbers found.")
    return sorted(primes)[-2]