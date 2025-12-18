"""
QUESTION:
Write a function `find_divisible_numbers` that takes a list of positive integers as input. The function should return a tuple containing the highest and lowest numbers in the list. If the highest number is divisible by the lowest number, the highest number should be the first element of the tuple, otherwise the lowest number should be the first element. If the list is empty or contains only one element, the function should return None.
"""

def find_divisible_numbers(numbers):
    if len(numbers) < 2:
        return None

    highest = max(numbers)
    lowest = min(numbers)

    if highest % lowest == 0:
        return (highest, lowest)
    else:
        return (lowest, highest)