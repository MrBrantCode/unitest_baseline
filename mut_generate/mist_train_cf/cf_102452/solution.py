"""
QUESTION:
Develop a function merge_lists(l1, l2) that merges two lists l1 and l2 into a single list with unique elements. The function should remove duplicate elements from both l1 and l2, combine the resulting lists, and then remove any remaining duplicates. The merged list should be sorted in ascending order. The function should be able to handle lists containing integers and strings.
"""

def merge_lists(l1, l2):
    # Remove duplicates from l1 and l2
    l1 = list(set(l1))
    l2 = list(set(l2))
    
    # Merge l1 and l2
    merged_list = l1 + l2
    
    # Remove duplicates from the merged list
    merged_list = list(set(merged_list))
    
    # Sort the merged list in ascending order
    merged_list.sort()
    
    return merged_list