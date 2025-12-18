"""
QUESTION:
Write a function `get_max(numbers)` that accepts a list of numbers and returns the maximum number in the list. The function should handle the case where the input list is empty.
"""

def get_max(numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num