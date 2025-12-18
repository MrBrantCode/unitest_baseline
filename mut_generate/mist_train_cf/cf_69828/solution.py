"""
QUESTION:
Create a function `descending_squares` that takes a list of integers as input, squares each element, sorts the results in descending order, and returns the list. The function should handle edge cases correctly and produce the expected output.
"""

def descending_squares(numbers: list):
    """Should return descending list of squared values"""
    # Square each element
    squared_numbers = [num ** 2 for num in numbers]
    
    # Sort results in descending order
    squared_numbers.sort(reverse=True)

    return squared_numbers