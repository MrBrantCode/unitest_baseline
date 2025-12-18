"""
QUESTION:
Design a function `check_ordered_list(lst)` that checks if a given list `lst` is ordered in an increasing order. If the list is not ordered, count the number of times the order changes within the list. The function should return a string stating whether the list is ordered or not and include the number of order changes if applicable. Assume the list contains at least two elements.
"""

def check_ordered_list(lst):
    is_ordered = True
    order_changes = 0
    
    for i in range(len(lst) - 1):
        if lst[i] >= lst[i+1]:
            is_ordered = False
            order_changes += 1
    
    if is_ordered:
        return "The list is ordered in an increasing order."
    else:
        return "The list is not ordered in an increasing order and the order changes " + str(order_changes) + " time(s)." 