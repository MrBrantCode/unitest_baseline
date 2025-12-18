"""
QUESTION:
Create a function named `median_non_primes` that takes a list of numbers as input. The function should return the median of the numbers in the list, excluding any prime numbers and numbers outside the range of 1-50. The function should handle exceptions when the input list is empty or contains non-numeric characters.
"""

import statistics

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def median_non_primes(numbers):
    try:
        non_primes = [num for num in numbers if 1 <= num <= 50 and not is_prime(num)]
        if not non_primes: 
            return "Empty list of non-prime numbers"
        return statistics.median(non_primes)
    except TypeError:
        return 'Invalid item in the list'
    except Exception as e: 
        return str(e)