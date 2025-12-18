"""
QUESTION:
Define a function `find_highest_and_lowest(numbers)` that takes a list of positive integers `numbers` as input and returns a tuple with the highest and lowest numbers. The function should return the tuple with the highest number as the first element and the lowest number as the second element if the highest number is divisible by the lowest number or if the lowest number is prime. Otherwise, the function should return the tuple with the lowest number as the first element and the highest number as the second element. If the list is empty or contains only one element, the function should return `None`. The time complexity of the solution should not exceed O(n^2), where n is the length of the list.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def entance(numbers):
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