"""
QUESTION:
Write a function named `closest_number_index` that takes three parameters: a list of numbers, a target number, and a target value. The function should return the index of the first occurrence of the number in the list that is closest to the target value. If the target number is not found in the list, the function should return -1. The function should handle cases where the input list is empty, contains duplicate numbers, is not sorted, or contains negative or float numbers.
"""

def closest_number_index(lst, num, target):
    """
    Returns the index of the first occurrence of the number in the list that is closest to the target value.
    
    Parameters:
    lst (list): A list of numbers
    num (int): Target number
    target (int): Target value
    
    Returns:
    int: The index of the closest number, or -1 if not found
    """
    if len(lst) == 0:
        return -1

    closest_index = -1
    closest_difference = float('inf')

    for i, n in enumerate(lst):
        difference = abs(n - target)
        if difference < closest_difference:
            closest_difference = difference
            closest_index = i

    return closest_index