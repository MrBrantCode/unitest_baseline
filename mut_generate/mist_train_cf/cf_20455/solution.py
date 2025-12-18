"""
QUESTION:
Write a function `count_target_occurrences` that takes two parameters: a list of integers (`lst`) and a target integer (`target`). The function should return the number of times the target integer appears in the list. The list may contain duplicate elements and must have at least 1 element (error message should be returned for an empty list). The target integer will be within the range of -1000 to 1000.
"""

def count_target_occurrences(lst, target):
    """
    This function counts the number of times the target integer appears in the list.
    
    Parameters:
    lst (list): A list of integers.
    target (int): The target integer to be searched.
    
    Returns:
    int or str: The count of target occurrences if the list is not empty, otherwise an error message.
    """
    if not lst:
        return "Error: The list is empty."
    
    count = 0
    for num in lst:
        if num == target:
            count += 1
    
    return count