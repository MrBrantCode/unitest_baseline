"""
QUESTION:
Write a function `find_min_max(numbers)` that takes a list of numbers as input and returns a tuple containing the minimum and maximum elements. The function should not use any built-in functions or methods for finding the minimum and maximum. The function should handle the case where the input list is empty, in which case it should return `(None, None)`.
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