"""
QUESTION:
Write a function `find_highest_and_lowest(numbers)` that takes a list of positive integers as input. The function should return a tuple with the highest and lowest numbers in the list, ordered based on the following conditions:

- If the list is empty or contains only one element, return None.
- If the highest number is divisible by the lowest number, return a tuple with the highest number as the first element and the lowest number as the second element.
- If the lowest number is a prime number, return a tuple with the highest number as the first element and the lowest number as the second element.
- Otherwise, return a tuple with the lowest number as the first element and the highest number as the second element.

The function should have a time complexity of no worse than O(n^2), where n is the length of the list.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_highest_and_lowest(numbers):
    if len(numbers) < 2:
        return None
    highest = numbers[0]
    lowest = numbers[0]
    for num in numbers[1:]:
        if num > highest:
            highest = num
        if num < lowest:
            lowest = num
    if highest % lowest == 0:
        return (highest, lowest)
    if is_prime(lowest):
        return (highest, lowest)
    return (lowest, highest)