"""
QUESTION:
Create a function named `sum_valid_numbers` that takes a list of strings representing numerical data and returns the sum of all valid numbers. The function should handle strings in the format of integers, decimals, and scientific notation. If the list contains any non-numeric strings, the function should return an error message "Invalid data type at index {i}", where {i} is the index of the first invalid data.
"""

def sum_valid_numbers(data):
    total = 0
    for i, num in enumerate(data):
        try:
            total += float(num)
        except ValueError:
            return f"Invalid data type at index {i}"
    return total