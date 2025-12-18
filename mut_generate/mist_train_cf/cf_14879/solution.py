"""
QUESTION:
Write a function `find_max_min` that takes a list of integers as input and returns a tuple of the maximum and minimum values in the list. The function should not use any built-in functions or methods to find the maximum and minimum values and should only iterate through the list once. If the input list is empty, the function should return `(None, None)`.
"""

def find_max_min(list_of_numbers):
    if len(list_of_numbers) == 0:
        return None, None

    max_value = list_of_numbers[0]
    min_value = list_of_numbers[0]

    for number in list_of_numbers:
        if number > max_value:
            max_value = number
        if number < min_value:
            min_value = number

    return max_value, min_value