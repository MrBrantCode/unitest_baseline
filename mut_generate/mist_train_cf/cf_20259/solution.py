"""
QUESTION:
Write a function called `find_largest_prime` that finds the largest prime number in an array of integers. The array can contain duplicate values and there may be multiple largest prime numbers, in which case any one of them can be returned. The function should be able to handle cases where there are no prime numbers in the array.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_largest_prime(numbers):
    largest_prime = None
    for num in numbers:
        if is_prime(num):
            if largest_prime is None or num > largest_prime:
                largest_prime = num
    return largest_prime