"""
QUESTION:
Create a function named `find_max` that takes an array of numbers as input and returns the element with the highest numerical value. Do not use any built-in functions for finding the maximum value, such as `max()`. The function should be able to handle an array of any size.
"""

def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num