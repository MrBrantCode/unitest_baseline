"""
QUESTION:
Create a function named `remove_elements` that takes a list of numbers and a value as input. The function should remove all elements of the list that are equal to the given value without using built-in list removal functions or methods (e.g. remove(), del, pop()). Instead, implement the removal logic manually. The function must modify the list in-place and return the modified list. The function should also handle edge cases where the list is empty or does not contain the given value, in which case it should return the original list unmodified.
"""

def remove_elements(list_of_numbers, value):
    """
    Removes all elements of the list that are equal to the given value in-place.
    
    Args:
    list_of_numbers (list): The list of numbers.
    value (int): The value to be removed.
    
    Returns:
    list: The modified list.
    """
    index = 0
    while index < len(list_of_numbers):
        if list_of_numbers[index] == value:
            list_of_numbers.pop(index)
        else:
            index += 1
    return list_of_numbers