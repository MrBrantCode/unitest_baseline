"""
QUESTION:
Write a function named `combine_lists` that takes two lists of unique integers in ascending order as input and returns a new list that combines the elements of both input lists in ascending order. The function should be able to handle lists of different lengths.
"""

def combine_lists(list_1, list_2):
    combined_list = []
    i = 0
    j = 0
    
    while i < len(list_1) and j < len(list_2):
        if list_1[i] < list_2[j]:
            combined_list.append(list_1[i])
            i += 1
        else:
            combined_list.append(list_2[j])
            j += 1
    
    while i < len(list_1):
        combined_list.append(list_1[i])
        i += 1
    
    while j < len(list_2):
        combined_list.append(list_2[j])
        j += 1
    
    return combined_list