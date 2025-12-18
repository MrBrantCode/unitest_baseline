"""
QUESTION:
Write a function `find_min_max` that takes a list of at least 5 numbers as input and returns a tuple containing the minimum and maximum values in the list without using built-in min() and max() functions. The list may contain duplicates and a mix of positive and negative numbers.
"""

def find_min_max(numbers):
    # Initialize the minimum and maximum values
    min_value = numbers[0]
    max_value = numbers[0]

    # Iterate through the list and update the minimum and maximum values if necessary
    for number in numbers:
        if number < min_value:
            min_value = number
        if number > max_value:
            max_value = number

    # Return the minimum and maximum values
    return min_value, max_value