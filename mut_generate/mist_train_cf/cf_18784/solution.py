"""
QUESTION:
Find the maximum number in a list of integers without using built-in functions or methods to determine the maximum value. The function `find_max_number(numbers)` should take a list of integers as input and return the maximum number. If the input list is empty, return the error message "List is empty."
"""

def find_max_number(numbers):
    if len(numbers) == 0:
        return "List is empty."
    
    max_number = float('-inf')
    for num in numbers:
        if num > max_number:
            max_number = num
    
    return max_number