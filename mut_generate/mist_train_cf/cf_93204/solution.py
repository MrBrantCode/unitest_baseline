"""
QUESTION:
Write a function called group_and_sum that takes a list of integers and a condition as input, groups the integers based on whether they satisfy the condition, and returns a dictionary where the keys are the condition outcomes (True or False) and the values are the sums of the integers in each group.
"""

def group_and_sum(numbers, condition):
    """
    Groups a list of numbers based on a given condition and returns a dictionary 
    with the condition outcomes as keys and the sums of the numbers in each group as values.

    Args:
        numbers (list): A list of integers.
        condition (function): A function that takes an integer and returns a boolean.

    Returns:
        dict: A dictionary with the condition outcomes as keys and the sums of the numbers in each group as values.
    """
    groups = {}
    for num in numbers:
        key = condition(num)
        if key in groups:
            groups[key].append(num)
        else:
            groups[key] = [num]

    return {key: sum(group) for key, group in groups.items()}