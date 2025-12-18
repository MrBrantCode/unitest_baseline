"""
QUESTION:
Write a function called `find_smallest_value` that takes a list of integers as input and returns the smallest number in the list.
"""

def find_smallest_value(numbers):
    smallest_value = numbers[0]
    for number in numbers:
        if number < smallest_value:
            smallest_value = number
    return smallest_value