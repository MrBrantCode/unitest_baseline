"""
QUESTION:
Write a function `get_maximum_number` that takes a list of numbers as input and returns the maximum number in the list, provided that the maximum number is not divisible by any number in the list other than 1 and itself. If the maximum number is divisible by another number in the list, return a message indicating this. The function should ignore duplicate numbers in the list.
"""

def get_maximum_number(numbers):
    # Remove duplicate numbers from the list
    unique_numbers = list(set(numbers))

    # Find the maximum number
    max_number = max(unique_numbers)

    # Check if the maximum number is divisible by any other number in the list
    for num in unique_numbers:
        if num != max_number and max_number % num == 0:
            return "Maximum number is divisible by a number other than 1 and itself"

    return max_number