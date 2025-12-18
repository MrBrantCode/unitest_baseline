"""
QUESTION:
Write a function named `calculate_average` that takes a list of numbers as input and returns the average of the numbers. The function should not use any built-in library or third-party modules for calculating the average. Implement a custom error-handling mechanism to validate the input list, ensuring that all elements are numbers. If an invalid input is found, return an error message.
"""

def calculate_average(lst):
    # Custom error-handling to validate the input
    if not all(isinstance(item, (int, float)) for item in lst):
        return "Error: All elements in the list must be numbers."
    
    # Calculate the average
    total = sum(lst)
    avg = total / len(lst)
    return avg