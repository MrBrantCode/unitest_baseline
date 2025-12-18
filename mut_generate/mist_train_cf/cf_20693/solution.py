"""
QUESTION:
Write a function named `custom_sort` that takes a list of items and an integer as input, and returns a list of items with a length less than or equal to the given number in ascending order. The function should not use any built-in sorting functions and have a time complexity of O(nlogn) or better.
"""

def custom_sort(list_items, given_number):
    """
    This function takes a list of items and an integer as input, 
    and returns a list of items with a length less than or equal to the given number in ascending order.

    Args:
        list_items (list): A list of items.
        given_number (int): The maximum length of items.

    Returns:
        list: A list of items with a length less than or equal to the given number in ascending order.
    """
    result = []
    for item in list_items:
        if len(str(item)) <= given_number:
            result.append(item)
    
    for i in range(len(result)):
        for j in range(i+1, len(result)):
            if result[i] > result[j]:
                result[i], result[j] = result[j], result[i]
    
    return result