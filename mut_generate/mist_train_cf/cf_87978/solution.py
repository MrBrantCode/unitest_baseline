"""
QUESTION:
Write a function `find_max_min` that takes a list of integers as input and returns a tuple containing the maximum and minimum number in the list. The function should have a time complexity of O(n), where n is the length of the list, and should not use any built-in functions or methods such as max(), min(), or sorting algorithms. The function should handle edge cases such as an empty list or a list with a single element, and should not modify the original list.
"""

def find_max_min(numbers):
    if len(numbers) == 0:
        return None, None
    if len(numbers) == 1:
        return numbers[0], numbers[0]

    max_num = numbers[0]
    min_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    return max_num, min_num