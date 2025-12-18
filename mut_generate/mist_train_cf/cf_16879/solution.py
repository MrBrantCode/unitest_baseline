"""
QUESTION:
Create a function called `sum_positive_elements` that calculates the sum of all elements in the input data, which can be an array or a list. The data must contain at least 3 and at most 10 elements, and all elements must be non-negative numbers. If these conditions are not met, return an error message.
"""

def sum_positive_elements(data):
    if len(data) < 3 or len(data) > 10:
        return "Invalid data length"
    if any(num < 0 for num in data):
        return "Data contains negative numbers"
    
    return sum(data)