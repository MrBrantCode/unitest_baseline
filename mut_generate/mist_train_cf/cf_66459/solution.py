"""
QUESTION:
Write a function `sort_dict_by_last_digit` that takes a dictionary as input, where the keys are integers. The function should return a new dictionary sorted by the last digit of each key. If two keys have the same last digit, their original order should be maintained. The function should work for both positive and negative integers.
"""

def sort_dict_by_last_digit(input_dict):
    """
    Sorts a dictionary by the last digit of each key.

    Args:
    input_dict (dict): A dictionary with integer keys.

    Returns:
    dict: A new dictionary sorted by the last digit of each key.
    """
    return {k: input_dict[k] for k in sorted(input_dict, key=lambda x: abs(x) % 10)}