"""
QUESTION:
Implement a function called `remove_duplicates` that takes a list of elements as input and returns a new list with all recurring instances removed, preserving the original order of elements. The function should be able to handle lists containing any type of elements, not just integers.
"""

def remove_duplicates(numbers):
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers