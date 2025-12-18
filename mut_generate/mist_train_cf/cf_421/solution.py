"""
QUESTION:
Create a function called `find_min_max` that takes a list of numbers as input and returns the minimum and maximum values in the list. The function should not use built-in `min()` and `max()` functions, should iterate through the list only once, and should have a time complexity of O(n). The input list will have at least one element and may contain duplicates and both positive and negative numbers.
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