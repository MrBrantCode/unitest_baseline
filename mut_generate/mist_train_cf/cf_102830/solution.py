"""
QUESTION:
Write a function `count_and_remove` that takes a list of integers and a target number as input. The function should return the count of the target number in the list and the updated list with all occurrences of the target number removed.
"""

def count_and_remove(lst, target):
    """
    This function takes a list of integers and a target number as input.
    It returns the count of the target number in the list and the updated list with all occurrences of the target number removed.
    
    Parameters:
    lst (list): A list of integers.
    target (int): The target number to be counted and removed.
    
    Returns:
    tuple: A tuple containing the count of the target number and the updated list.
    """
    count = lst.count(target)
    updated_list = [x for x in lst if x != target]
    return count, updated_list