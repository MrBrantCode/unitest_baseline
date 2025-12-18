"""
QUESTION:
Create a function `find_divisible_numbers(numbers)` that takes a list of positive integers `numbers` as input and returns a tuple containing the highest and lowest numbers. The function should order the tuple so that if the highest number is divisible by the lowest number, the highest number is first; otherwise, the lowest number is first. If the input list contains fewer than two elements, the function should return `None`.
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