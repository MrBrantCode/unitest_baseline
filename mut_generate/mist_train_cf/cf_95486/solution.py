"""
QUESTION:
Write a function `group_and_sort` that takes a list of positive integers as input and returns a list of lists, where each inner list contains the numbers with the same last digit, sorted in ascending order. The function should group the numbers based on their last digit and then sort each group in ascending order.
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