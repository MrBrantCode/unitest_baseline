"""
QUESTION:
Create a function `create_dictionary(list1, list2)` that takes two lists as arguments and returns a dictionary. The function should use elements of `list1` as keys and elements of `list2` as values. If the lists are of unequal length, use elements from the longer list as keys and elements from the shorter list as values, cycling through the shorter list as necessary. If a key in `list1` already exists in the dictionary, do not overwrite its value. If both lists are empty, return an empty dictionary.
"""

def create_dictionary(list1, list2):
    dictionary = {}
    
    if len(list1) == 0 and len(list2) == 0:
        return dictionary
    
    if len(list1) >= len(list2):
        for i in range(len(list1)):
            if i < len(list2):
                if list1[i] not in dictionary:
                    dictionary[list1[i]] = list2[i]
    else:
        for i in range(len(list2)):
            if i < len(list1):
                if list1[i] not in dictionary:
                    dictionary[list1[i]] = list2[i]
    
    return dictionary