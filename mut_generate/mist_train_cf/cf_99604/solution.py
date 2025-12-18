"""
QUESTION:
Create a function named `sum_valid_numbers` that takes a list of strings representing numerical data as input. The function should return the sum of all valid numbers in the list. A valid number is one that can be converted to a float. If an invalid number is encountered, return an error message in the format "Invalid data type at index {i}", where {i} is the index of the invalid data.
"""

def sum_valid_numbers(data):
    total = 0
    for i, num in enumerate(data):
        try:
            total += float(num)
        except ValueError:
            return f"Invalid data type at index {i}"
    return total