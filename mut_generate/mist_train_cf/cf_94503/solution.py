"""
QUESTION:
Create a function called `add_and_average` that takes two lists of integers as input, merges them, removes duplicates, sorts the resulting list in ascending order, and calculates the average of the resulting list. The function should return the sorted list and its average. The input lists are guaranteed to contain unique integers in ascending order.
"""

def add_and_average(list1, list2):
    # Merge the two lists
    merged_list = list1 + list2
    
    # Sort the merged list in ascending order and remove duplicates
    sorted_unique_list = sorted(set(merged_list))
    
    # Calculate the average of the sorted unique list
    average = sum(sorted_unique_list) / len(sorted_unique_list)
    
    return sorted_unique_list, average