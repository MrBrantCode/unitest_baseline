"""
QUESTION:
Create a function named `sort_list_items` that takes two parameters: a list of integers (`list_items`) and an integer (`given_number`). The function should return a new list containing items from `list_items` with the number of digits less than or equal to `given_number`, in ascending order. The function should not use any built-in sorting functions.
"""

def sort_list_items(list_items, given_number):
    """
    Returns a new list containing items from list_items with the number of digits 
    less than or equal to given_number, in ascending order.

    Args:
    list_items (list): A list of integers.
    given_number (int): The maximum number of digits.

    Returns:
    list: A new list containing items from list_items with the number of digits 
    less than or equal to given_number, in ascending order.
    """
    sorted_list = []
    for item in list_items:
        if len(str(item)) <= given_number:
            sorted_list.append(item)
    for i in range(len(sorted_list)-1):
        for j in range(i+1, len(sorted_list)):
            if sorted_list[i] > sorted_list[j]:
                sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]
    return sorted_list