"""
QUESTION:
Write a function `find_average` that calculates the average of numbers in a list, excluding strings and considering only numbers in the list. The list may contain nested lists and dictionaries, which should also be excluded from the calculation, but numbers within these nested structures should be included. The function should take a list as an input and return the calculated average. The input list may contain a mix of integers, floats, strings, lists, and dictionaries.
"""

def find_average(lst):
    """
    Calculate the average of numbers in a list, excluding strings and considering only numbers in the list.
    The list may contain nested lists and dictionaries, which should also be excluded from the calculation,
    but numbers within these nested structures should be included.

    Args:
        lst (list): A list containing a mix of integers, floats, strings, lists, and dictionaries.

    Returns:
        float: The calculated average of numbers in the list.
    """
    numbers = []
    for item in lst:
        if isinstance(item, (int, float)):
            numbers.append(item)
        elif isinstance(item, list):
            numbers.extend([num for num in item if isinstance(num, (int, float))])
        elif isinstance(item, dict):
            numbers.extend([value for value in item.values() if isinstance(value, (int, float))])
    if len(numbers) == 0:
        return 0
    average = sum(numbers) / len(numbers)
    return average