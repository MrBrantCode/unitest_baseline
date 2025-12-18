"""
QUESTION:
Implement a function named "sort_dictionaries" that takes a list of dictionaries as input, where each dictionary contains a single key-value pair. The function should return a new sorted list of dictionaries. The sorting should be done based on the values of the keys in descending order. If two dictionaries have the same value, they should be sorted based on the length of their keys in ascending order. If the lengths are also the same, the dictionaries should be sorted alphabetically by their keys in descending order. The original list should remain unchanged after sorting.
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