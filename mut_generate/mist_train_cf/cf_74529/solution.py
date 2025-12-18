"""
QUESTION:
Develop a function `validate_and_add(arr)` that takes an array `arr` as input and returns the sum of all elements in the array if all elements are numerical values (either integers or floats), otherwise returns a message indicating that the array contains non-numerical values.
"""

def validate_and_add(arr):
    if all(isinstance(i, (int, float)) for i in arr):
        return sum(arr)
    else:
        return "Array contains non-numerical values."