"""
QUESTION:
Create a function named `squares_dictionary` that takes a list of mixed data types as input and returns a dictionary where keys are the numbers from the list and their corresponding values are the squares of these numbers. The function should ignore non-numeric values in the list and handle both integers and floats. The solution should be efficient in terms of time complexity.
"""

def entrance(numbers):
    return {num: num*num for num in numbers if isinstance(num, (int, float))}