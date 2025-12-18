"""
QUESTION:
Create a function called `find_highest_value` that takes a list of numerical values as input, including integers, floating point numbers, and negative numbers, and returns the highest numerical value in the list without using the built-in `max()` function or any sorting algorithms.
"""

def find_highest_value(numbers):
    highest_value = numbers[0]
    for number in numbers:
        if number > highest_value:
            highest_value = number
    return highest_value