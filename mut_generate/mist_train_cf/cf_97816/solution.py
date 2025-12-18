"""
QUESTION:
Create a function named `sum_valid_numbers` that takes a list of strings as input, where each string represents a numerical value. The function should return the sum of all valid numbers in the list. A valid number is a string that can be successfully converted to a float. If a string cannot be converted to a float, the function should return an error message in the format "Invalid data type at index X", where X is the index of the invalid data in the input list.
"""

def sum_valid_numbers(data):
    total = 0
    for i, num in enumerate(data):
        try:
            total += float(num)
        except ValueError:
            return f"Invalid data type at index {i}"
    return total