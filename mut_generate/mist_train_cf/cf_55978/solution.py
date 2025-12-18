"""
QUESTION:
Create a Python function named `sort_three_dimensional_list` that takes a three-dimensional list as input and sorts the sublists based on the third value in each sub-sublist. The function should return the sorted three-dimensional list. Each sublist in the main list should be sorted independently.
"""

from operator import itemgetter

def sort_three_dimensional_list(three_d_list):
    # Initialize empty list to store sorted list
    sorted_list = []
    
    # Iterate over the main list
    for sub_list in three_d_list:
        # Sort each sub_list per the third value in the sub_sub_list
        sorted_sub_list = sorted(sub_list, key=itemgetter(2))
        
        # Append sorted sub_list to the main sorted list
        sorted_list.append(sorted_sub_list)
    
    return sorted_list