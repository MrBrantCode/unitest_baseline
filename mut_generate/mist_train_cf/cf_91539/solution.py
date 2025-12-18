"""
QUESTION:
Implement a function named `remove_duplicates` that takes a list as input and returns a new list containing the same elements in the original order but without duplicates.
"""

def remove_duplicates(original_list):
    unique_list = []
    for element in original_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list