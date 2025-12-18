"""
QUESTION:
Write a function `find_max_min` that takes a list of numbers as input and returns the maximum and minimum numbers in the list. The function should not use any built-in functions or methods such as `max()`, `min()`, or sorting algorithms, and should have a time complexity of O(n), where n is the length of the list. If the list is empty, the function should return `None` for both the maximum and minimum numbers.
"""

def find_max_min(numbers):
    if len(numbers) == 0:
        return None, None

    max_num = numbers[0]
    min_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    return max_num, min_num