"""
QUESTION:
Write a function named `filter_and_check_prime` that takes a list of integers as input. The function should filter out the numbers that are divisible by both 3 and 5, calculate the sum of the filtered numbers, and check if the sum is a prime number. If the sum is prime, return the filtered numbers as a list; otherwise, return an empty list.
"""

from functools import reduce

def filter_and_check_prime(numbers):
    def check_prime(n):
        if n == 1:
            return False
        elif n == 2:
            return True
        else:
            for x in range(2, n):
                if (n % x) == 0:
                    return False
            return True

    filtered_numbers = list(filter(lambda x: (x % 3 == 0 and x % 5 == 0), numbers))
    sum_of_numbers = reduce(lambda a, b: a + b, filtered_numbers) if filtered_numbers else 0

    return filtered_numbers if check_prime(sum_of_numbers) else []