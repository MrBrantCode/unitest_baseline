"""
QUESTION:
Write a function called `exchange_and_remove_duplicates` that takes a list as input, swaps its first and last elements, removes any duplicate elements while maintaining the order of the remaining elements, and returns the modified list.
"""

def exchange_and_remove_duplicates(lst):
    # Swap the first and last elements
    if len(lst) > 1:
        lst[0], lst[-1] = lst[-1], lst[0]
    
    # Remove duplicates while maintaining order
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    
    return unique_lst