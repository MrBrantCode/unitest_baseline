"""
QUESTION:
Write a function `find_min_max(numbers)` that takes a list of numbers as input and returns the lowest and highest numbers in the list without using built-in functions like `max()` and `min()`. The list can contain negative numbers and decimals.
"""

def find_min_max(numbers):
    min_num = numbers[0]
    max_num = numbers[0]
    for number in numbers:
        if number < min_num:
            min_num = number
        if number > max_num:
            max_num = number
    return min_num, max_num