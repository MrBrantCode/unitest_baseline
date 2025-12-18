"""
QUESTION:
Design a function named `check_order` that takes a list of integers as input. The function should return a message indicating whether the list is ordered in increasing order and the number of times the order changes. If the list is ordered in increasing order, the function should return a message stating so. If the list is not ordered in increasing order, the function should return a message stating that the list is not ordered and the number of times the order changes.
"""

def check_order(lst):
    """
    Checks if a list of integers is ordered in increasing order.

    Args:
        lst (list): A list of integers.

    Returns:
        str: A message indicating whether the list is ordered in increasing order and the number of times the order changes.
    """
    order_changes = 0
    for i in range(len(lst) - 1):
        if lst[i] >= lst[i+1]:
            order_changes += 1
    if order_changes == 0:
        return "The list is ordered in an increasing order"
    else:
        return f"The list is not ordered in an increasing order and the order changes {order_changes} time(s)"