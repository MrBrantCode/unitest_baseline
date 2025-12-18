"""
QUESTION:
Create a function `get_maximum_number` that takes a list of numbers as input. The function should return the maximum number in the list that is not divisible by any other number in the list, except for 1 and itself. The function should ignore duplicate numbers in the list. If no such number exists, return a message indicating that the maximum number is divisible by a number other than 1 and itself.
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