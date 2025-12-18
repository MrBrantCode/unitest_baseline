"""
QUESTION:
Write a function named `remove_duplicates` that takes a list as input and returns a new list with all duplicate elements removed. The function should not use any built-in Python functions or libraries and should have a time complexity of O(n), where n is the length of the list. The input list can contain any type of elements.
"""

def remove_duplicates(lst):
    # Create an empty dictionary to keep track of the unique elements
    unique_dict = {}

    # Iterate through the list
    for element in lst:
        # Check if the element is already in the dictionary
        if element not in unique_dict:
            # If not, add it to the dictionary
            unique_dict[element] = True

    # Create a new list with the unique elements
    unique_lst = []
    for key in unique_dict:
        unique_lst.append(key)

    # Return the new list without duplicates
    return unique_lst