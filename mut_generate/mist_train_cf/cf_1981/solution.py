"""
QUESTION:
Create a function `remove_duplicates(input_list)` that removes all duplicates from a list while maintaining the original order of elements without using any built-in Python functions or libraries, excluding set and dictionary. The function should return a new list containing the unique elements from the input list.
"""

def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list