"""
QUESTION:
Create a function named `create_dictionary` that takes two lists, `list1` and `list2`, as input and returns a dictionary where the keys are the elements of `list1` and the values are the corresponding elements of `list2`. The function should handle lists of any length but must return an error message if the input lists are not of equal length.
"""

def create_dictionary(list1, list2):
    if len(list1) != len(list2):
        return "Error: Lists should have equal length"
    
    dictionary = {}
    for i in range(len(list1)):
        dictionary[list1[i]] = list2[i]
    
    return dictionary