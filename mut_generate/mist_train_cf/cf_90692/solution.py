"""
QUESTION:
Write a function `find_min_max(numbers)` that takes a list of numbers as input and returns the minimum and maximum elements in the list without using any built-in functions or methods for finding the minimum and maximum. If the list is empty, return `None` for both the minimum and maximum values.
"""

def find_min_max(numbers):
    if len(numbers) == 0:
        return None, None  

    min_num = max_num = numbers[0]  

    for num in numbers:
        if num < min_num:
            min_num = num  
        if num > max_num:
            max_num = num  

    return min_num, max_num