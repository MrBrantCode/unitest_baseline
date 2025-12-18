"""
QUESTION:
Implement a function named `find_max_number` that takes a list of integers as input and returns the maximum number in the list. The function must not use any built-in functions or methods to find the maximum value and should handle the case where the list is empty by returning an error message.
"""

def find_max_number(numbers):
    if len(numbers) == 0:
        return "List is empty."
    
    max_number = float('-inf')
    for num in numbers:
        if num > max_number:
            max_number = num
    
    return max_number