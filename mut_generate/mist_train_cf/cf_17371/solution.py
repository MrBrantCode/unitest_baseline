"""
QUESTION:
Create a function named `group_numbers` that takes two parameters: an array of numbers and a list of conditions where each condition is a function. Group the numbers in the array based on the conditions. A number can be included in a group if it satisfies the corresponding condition. Return a dictionary where the keys are 'Group 1', 'Group 2', etc. and the values are lists of numbers that satisfy the corresponding condition.
"""

def group_numbers(array, conditions):
    """
    Group numbers in the array based on the given conditions.

    Args:
        array (list): A list of numbers to be grouped.
        conditions (list): A list of functions where each function represents a condition.

    Returns:
        dict: A dictionary where keys are 'Group 1', 'Group 2', etc. and values are lists of numbers that satisfy the corresponding condition.
    """
    groups = {}
    for i, condition in enumerate(conditions):
        group = [num for num in array if condition(num)]
        groups[f"Group {i+1}"] = group
    return groups