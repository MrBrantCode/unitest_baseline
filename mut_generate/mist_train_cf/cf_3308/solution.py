"""
QUESTION:
Write a function `sum_of_numbers` that takes a list of strings as input and returns the sum of all the numbers in the list. If any string in the list is not numeric, raise a custom exception with the error message "Invalid input: {string} is not a number". The function must have a time complexity of O(n), where n is the number of elements in the list.
"""

class CustomException(Exception):
    pass

def sum_of_numbers(strings):
    total = 0
    for string in strings:
        try:
            total += int(string)
        except ValueError:
            raise CustomException(f"Invalid input: {string} is not a number")
    return total