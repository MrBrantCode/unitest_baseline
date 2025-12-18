"""
QUESTION:
Write a function `largest_divisor(n: int) -> int` that takes an integer `n` and returns the largest number that divides `n` completely but is smaller than `n`. The function should handle edge cases such as `n` being less than 2 and negative numbers.

Write a second function `largest_divisors_of_list(numbers: List[int]) -> List[int]` that takes a list of integers `numbers` and returns a new list containing the largest divisors of the absolute values of each integer in the original list. The function should handle edge cases such as an empty list.

Both functions should be efficient and provide the correct output for all valid inputs.
"""

from typing import List

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, yet, is smaller than n"""
    # convert the number to absolute
    n = abs(n)
    if n < 2:
        return None
    # Check for all divisors starting from half of the number
    for i in range(n//2, 0, -1): 
        if n % i == 0:
            return i

def largest_divisors_of_list(numbers: List[int]) -> List[int]:
    """ For a given list of integers, find the largest absolute divisors for each integer and return a new list with these values"""
    # check for null list
    if not numbers:
        return None
    largest_divisors = []
    # for each number in the list, find the largest divisor and append to the output list
    for num in numbers:
        largest_divisors.append(largest_divisor(num))
    return largest_divisors