"""
QUESTION:
Design a function `check_order` that checks if a given list of numbers is ordered in increasing order and counts the number of times the order changes. The function should return a message indicating whether the list is ordered and the number of times the order changes. The list is considered ordered in increasing order if each element is less than or equal to the next element.
"""

def check_order(lst):
    """
    This function checks if a given list of numbers is ordered in increasing order 
    and counts the number of times the order changes.

    Args:
        lst (list): A list of numbers.

    Returns:
        str: A message indicating whether the list is ordered and the number of times the order changes.
    """
    is_ordered = True
    order_changes = 0
    
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            is_ordered = False
            order_changes += 1
            
    if is_ordered:
        return "The list is ordered in an increasing order and the order changes 0 times."
    else:
        return "The list is not ordered in an increasing order and the order changes {} times.".format(order_changes)