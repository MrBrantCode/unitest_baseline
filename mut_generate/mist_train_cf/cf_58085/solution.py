"""
QUESTION:
Write a function named `remove_duplicates` that accepts a list of numerical values as input and returns a new list with duplicate values removed, preserving the original order of elements.
"""

def remove_duplicates(list_of_numbers):
    result = []
    for number in list_of_numbers:
        if number not in result:
            result.append(number)
    return result