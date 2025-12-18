"""
QUESTION:
Create a function named `remove_duplicates_sort_list` that takes a list as input. The function should remove all non-integer elements from the list, remove any duplicate integers, and sort the resulting list in descending order. The function should be able to handle large input lists with up to 1,000,000 elements efficiently.
"""

def remove_duplicates_sort_list(input_list):
    unique_set = set()
    result = []
    
    for element in input_list:
        if isinstance(element, int):
            unique_set.add(element)
    
    for element in unique_set:
        result.append(element)
    
    result.sort(reverse=True)
    return result