"""
QUESTION:
Write a function named `find_second_largest` that takes a list of numbers as input. The function should return the second largest number in the list. Do not use any built-in sorting functions or functions that directly find the maximum or minimum value in the list, such as `sort()`, `sorted()`, `max()`, or `min()`. If the list has less than 2 elements, the function should return `None`.
"""

def find_second_largest(numbers):
    if len(numbers) < 2:
        return None
    
    largest = float('-inf')
    second_largest = float('-inf')
    
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    return second_largest