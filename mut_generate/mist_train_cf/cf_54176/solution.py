"""
QUESTION:
Create a function `sum_of_squares_is_prime_in_ranges` that checks if the sum of squares of every element in multiple lists of integers falls within different specified ranges and this sum is a prime number. The function takes two parameters: `lists`, a list of lists containing integers, and `ranges`, a list of ranges. It is assumed that the lengths of `lists` and `ranges` are the same.
"""

import math

def sum_of_squares_is_prime_in_ranges(lists: list, ranges: list):
    """
    Checks if the sum of squares of every element in multiple lists of integers falls
    within different specified ranges and this sum is a prime number.
    Args:
    lists: List of lists containing integers.
    ranges: List of ranges.
    Returns:
    List of booleans indicating if sum of squares of every element in multiple
    lists falls within different specified ranges and this sum is a prime number.
    """
    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    results = []
    for idx, list in enumerate(lists):
        sum_of_squares = sum([i**2 for i in list])
        if ranges[idx][0] <= sum_of_squares <= ranges[idx][1] and is_prime(sum_of_squares):
            results.append(True)
        else:
            results.append(False)
    return results