"""
QUESTION:
Write a function called `calculate_sum_and_average` that calculates the sum and average of integers in a given list. The list may contain both integers and strings, but only consider the integers for the calculation. If the list is empty or contains no integers, handle the error and return a meaningful result.
"""

def calculate_sum_and_average(array):
    """
    Calculate the sum and average of integers in a given list.

    Args:
    array (list): A list that may contain both integers and strings.

    Returns:
    tuple: A tuple containing the sum and average of integers in the list. 
           If the list is empty or contains no integers, returns (None, None).

    """
    total_sum = 0
    count = 0

    for num in array:
        if isinstance(num, int):
            total_sum += num
            count += 1
        elif isinstance(num, str) and num.isdigit():
            total_sum += int(num)
            count += 1

    if count == 0:
        return None, None
    else:
        average = total_sum / count
        return total_sum, average