"""
QUESTION:
Write a function `find_max_min` that finds the maximum and minimum numbers in a list without using built-in functions or methods such as `max()`, `min()`, or sorting algorithms. The function should have a time complexity of O(n), where n is the length of the list. The function should return `None` for both the maximum and minimum if the input list is empty.
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