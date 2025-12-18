"""
QUESTION:
Write a function `remove_duplicates` that takes a list `lst` of any type of elements as input and returns a new list containing the unique elements from `lst`, without using any built-in Python functions or libraries. The function should achieve this in a time complexity of O(n), where n is the length of the list.
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