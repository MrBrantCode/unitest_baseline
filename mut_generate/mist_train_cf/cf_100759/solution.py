"""
QUESTION:
Write a function `find_second_largest(numbers)` that takes a list of numbers as input and returns the second largest unique number in the list. If the list contains less than two unique numbers, the function should return `None`.
"""

def entrance(numbers):
    # Remove duplicates from the list
    unique_numbers = list(set(numbers))
    # Sort the list in descending order
    sorted_numbers = sorted(unique_numbers, reverse=True)
    # Return the second largest number
    if len(sorted_numbers) > 1:
        return sorted_numbers[1]
    else:
        return None