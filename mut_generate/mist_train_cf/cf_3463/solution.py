"""
QUESTION:
Write a function `find_max_min` that takes a list of integers as input and returns the maximum and minimum numbers in the list. The function should have a time complexity of O(n), where n is the length of the list, and should not use any built-in functions or methods such as max(), min(), or sorting algorithms. The function should handle edge cases, including an empty list, a list with a single element, and a list with duplicate, negative, zero, and positive numbers. The function should not modify the original list.
"""

def find_max_min(numbers):
    # Handle edge cases
    if len(numbers) == 0:
        return None, None
    if len(numbers) == 1:
        return numbers[0], numbers[0]

    # Initialize max and min variables
    max_num = numbers[0]
    min_num = numbers[0]

    # Iterate through the list
    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    return max_num, min_num