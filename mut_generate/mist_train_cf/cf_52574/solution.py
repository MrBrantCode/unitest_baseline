"""
QUESTION:
Write a function `find_values(lst)` that takes a list of integers as an argument. The function should return the highest value, lowest value, second highest value, and second lowest value in the list, as well as the difference between the second highest and second lowest values. If the list contains less than four unique numbers, the function should return an error message. The function should not use sorting or any built-in Python functions that find max or min values.
"""

def find_values(lst):
    """
    This function takes a list of integers and returns the highest value, lowest value, 
    second highest value, second lowest value, and the difference between the second 
    highest and second lowest values.

    Args:
        lst (list): A list of integers.

    Returns:
        tuple: A tuple containing the highest, lowest, second highest, second lowest values, 
        and the difference between the second highest and second lowest values.
        If the list contains less than four unique numbers, returns an error message.
    """
    if len(set(lst)) < 4:
        return "Error: list must contain at least four unique numbers"
    highest = second_highest = float('-inf')
    lowest = second_lowest = float('inf')
    for i in lst:
        if i > highest:
            second_highest = highest
            highest = i
        elif second_highest < i < highest:
            second_highest = i
        if i < lowest:
            second_lowest = lowest
            lowest = i
        elif second_lowest > i > lowest:
            second_lowest = i
    difference = second_highest - second_lowest
    return highest, lowest, second_highest, second_lowest, difference