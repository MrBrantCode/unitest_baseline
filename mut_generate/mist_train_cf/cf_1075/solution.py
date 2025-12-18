"""
QUESTION:
Write a function `swap_first_last` that swaps the first and last elements of a given list of integers without using any built-in functions or methods, creating new variables or lists, or additional libraries or modules. The function should have a time complexity of O(1). If the list has only one or no elements, return it as is.
"""

def swap_first_last(numbers):
    if len(numbers) <= 1:
        return numbers
    
    numbers[0], numbers[-1] = numbers[-1], numbers[0]
    
    return numbers