"""
QUESTION:
Create a function named `find_min_max` that takes a list of numbers as input and returns a tuple containing the minimum and maximum values in the list. The function must iterate through the list only once and have a time complexity of O(n), without using built-in functions like `min()` and `max()`. The input list will always have at least one number and may contain duplicates and both positive and negative numbers.
"""

def find_min_max(numbers):
    if len(numbers) < 1:
        return None
    min_num = numbers[0]
    max_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    return min_num, max_num