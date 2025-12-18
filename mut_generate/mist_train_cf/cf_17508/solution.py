"""
QUESTION:
Implement the "sort_dictionaries" function that takes a list of single-key-value dictionaries as an input and returns a new sorted list of dictionaries. The sorting should be done in descending order based on the values of the keys. If two dictionaries have the same value for the key, they should be sorted in ascending order based on the length of their keys. If two dictionaries have the same value for the key and the same length of keys, they should be sorted alphabetically by the keys in descending order. The original list should remain unchanged after sorting. The function should not use any built-in sorting function.
"""

def sort_dictionaries(lst):
    # Create a copy of the original list to ensure it remains unchanged
    sorted_lst = lst.copy()
    
    # Implement bubble sort algorithm
    for i in range(len(sorted_lst)):
        for j in range(len(sorted_lst) - 1 - i):
            # Compare values of the keys in descending order
            if list(sorted_lst[j].values())[0] < list(sorted_lst[j + 1].values())[0]:
                sorted_lst[j], sorted_lst[j + 1] = sorted_lst[j + 1], sorted_lst[j]
            # If values of the keys are the same, compare lengths of keys in ascending order
            elif list(sorted_lst[j].values())[0] == list(sorted_lst[j + 1].values())[0]:
                if len(list(sorted_lst[j].keys())[0]) > len(list(sorted_lst[j + 1].keys())[0]):
                    sorted_lst[j], sorted_lst[j + 1] = sorted_lst[j + 1], sorted_lst[j]
                # If lengths of keys are the same, compare keys alphabetically in descending order
                elif len(list(sorted_lst[j].keys())[0]) == len(list(sorted_lst[j + 1].keys())[0]):
                    if list(sorted_lst[j].keys())[0] < list(sorted_lst[j + 1].keys())[0]:
                        sorted_lst[j], sorted_lst[j + 1] = sorted_lst[j + 1], sorted_lst[j]
    
    return sorted_lst