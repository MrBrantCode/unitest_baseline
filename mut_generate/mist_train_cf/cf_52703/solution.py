"""
QUESTION:
Write a function named `find_max` that takes an array of integers as input and returns the largest number in the array. The array has at least one element.
"""

def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num