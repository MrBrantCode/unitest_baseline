"""
QUESTION:
Design a function called `find_second_largest` that takes a list of numbers as input. The function should return the second largest unique number in the list. If the list contains less than two unique numbers, the function should return None.
"""

def find_second_largest(numbers):
    # Remove duplicates from the list
    unique_numbers = list(set(numbers))
    # Sort the list in descending order
    sorted_numbers = sorted(unique_numbers, reverse=True)
    # Return the second largest number
    if len(sorted_numbers) > 1:
        return sorted_numbers[1]
    else:
        return None