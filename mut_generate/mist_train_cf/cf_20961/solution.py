"""
QUESTION:
Design a function `check_order` that takes a list `lst` as input and checks if the list is ordered in increasing order. If the list is ordered, return that it is ordered and the order changes 0 times. If the list is not ordered, return that it is not ordered and the number of times the order changes.
"""

def check_order(lst):
    """
    Checks if a given list is ordered in increasing order and counts the number of times the order changes.
    
    Args:
        lst (list): The input list to be checked.
    
    Returns:
        tuple: A tuple containing a boolean indicating whether the list is ordered and an integer representing the number of times the order changes.
    """
    is_ordered = True
    order_changes = 0
    
    for i in range(len(lst)-1):
        if lst[i] >= lst[i+1]:
            is_ordered = False
            order_changes += 1
            
    if is_ordered:
        return (True, 0)
    else:
        return (False, order_changes)