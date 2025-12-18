"""
QUESTION:
Create a function called `create_dictionary` that takes two parameters: `list1` and `list2`, both of which are lists of equal length. Return a dictionary where the keys are the elements of `list1` and the values are the corresponding elements of `list2`. If `list1` and `list2` are not of equal length, return an error message.
"""

def create_dictionary(list1, list2):
    if len(list1) != len(list2):
        return "Error: Lists should have equal length"
    
    dictionary = {}
    for i in range(len(list1)):
        dictionary[list1[i]] = list2[i]
    
    return dictionary