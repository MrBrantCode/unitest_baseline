"""
QUESTION:
Write a function `sum_positive_elements` that calculates the sum of all elements in a given data structure (array or list) with the following restrictions:
- The data structure must contain at least 3 and at most 10 elements.
- All elements in the data structure must be non-negative numbers.
If the data structure does not meet these restrictions, return an error message.
"""

def sum_positive_elements(data):
    if len(data) < 3 or len(data) > 10:
        return "Invalid data length"
    if any(num < 0 for num in data):
        return "Data contains negative numbers"
    
    return sum(data)