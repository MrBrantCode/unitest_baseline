"""
QUESTION:
Write a function `group_and_sort` that takes a list of positive integers as input and returns a list of lists. The function should group the input numbers by their last digit and sort each group in ascending order. The output list should contain the groups in ascending order of their corresponding last digits.
"""

def group_and_sort(numbers):
    # Create an empty dictionary to store the groups
    groups = {}

    # Group the numbers based on their last digit
    for number in numbers:
        last_digit = number % 10
        if last_digit in groups:
            groups[last_digit].append(number)
        else:
            groups[last_digit] = [number]

    # Sort each group in ascending order
    for key in groups:
        groups[key].sort()

    # Convert the dictionary to a list of lists
    result = [groups[key] for key in sorted(groups.keys())]

    return result