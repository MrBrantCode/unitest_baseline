"""
QUESTION:
Create a function `combine_to_dict` that takes two lists as input parameters, checks if they have equal length, and then combines the elements of the lists into a single dictionary where the keys come from the first list and the values from the second list. The function should handle scenarios where the lists are not of equal length, one or both lists are empty, or the elements in the lists are not the appropriate types to create a dictionary. The function should be able to work with lists of arbitrary length.
"""

def combine_to_dict(list1, list2):
    # checking if both lists are not empty
    if not list1 or not list2: 
        return "One or both lists are empty"
    try: 
        # checking if lists are of equal length
        if len(list1) == len(list2):
            return {list1[i]: list2[i] for i in range(len(list1))}
        else:
            return "Lists are not of equal length"
    except TypeError:
        return "Elements in the lists are not appropriate to create a dictionary"