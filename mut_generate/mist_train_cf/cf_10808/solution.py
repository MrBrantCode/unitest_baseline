"""
QUESTION:
Create a function named `remove_duplicates` that takes a list of elements as input and returns a new list containing only the unique elements from the original list, maintaining their original order. Do not use any built-in functions that achieve this result directly.
"""

def entrance(original_list):
    unique_list = []
    for element in original_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list