"""
QUESTION:
Create a function `create_dictionary` that takes two lists as arguments and returns a dictionary. The function should use elements of the first list as keys and elements of the second list as values. If the lists are of unequal length, the function should use keys from the longer list and values from the shorter list. If both lists are empty, the function should return an empty dictionary. In cases where the values in the second list are not unique, the function should use the first occurrence of a value as the corresponding value in the dictionary. The function should not use any built-in functions or methods such as `zip()`, `dict()`, or `enumerate()` to create the dictionary.
"""

def create_dictionary(list1, list2):
    # Initialize an empty dictionary
    dictionary = {}

    # Get the lengths of the input lists
    len1 = len(list1)
    len2 = len(list2)

    # Determine the longer and shorter lists
    if len1 >= len2:
        longer_list = list1
        shorter_list = list2
    else:
        longer_list = list2
        shorter_list = list1

    # Iterate over the longer list
    for i in range(len(longer_list)):
        # Check if there is a corresponding element in the shorter list
        if i < len(shorter_list):
            # Use the first occurrence of the value as the corresponding value in the dictionary
            if longer_list[i] not in dictionary:
                dictionary[longer_list[i]] = shorter_list[i]
        else:
            # If there is no corresponding element in the shorter list, use None as the value
            if longer_list[i] not in dictionary:
                dictionary[longer_list[i]] = None

    return dictionary