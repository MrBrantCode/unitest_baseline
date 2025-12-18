"""
QUESTION:
Create a function named 'check_ascending_order' that takes one argument, a list of numerical values. The function should return True if the list is in ascending order, False otherwise. If the input is not a list, return "Input is not a list". If the list is empty, return "The list is empty". If the list contains non-numerical values, return "The list contains non-numerical values".
"""

def check_ascending_order(lst):
    # Check if input is a list
    if not isinstance(lst, list):
        return "Input is not a list"
    # Check if list is not empty
    if len(lst) == 0:
        return "The list is empty"
    # Check for numerical values in list
    for i in lst:
        if not (isinstance(i, int) or isinstance(i, float)):
            return "The list contains non-numerical values"
    # Check if list is in ascending order
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True