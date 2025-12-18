"""
QUESTION:
Create a function named `merge_sorted_lists` that takes two sorted lists, `l1` and `l2`, as input and returns a single sorted list. The function should not use any built-in Python list functions or set operations. Implement the function using recursion to achieve this task.
"""

def merge_sorted_lists(l1, l2, merged_list=[]): 
    if len(l1)==0: 
        return merged_list + l2 
    if len(l2)==0: 
        return merged_list + l1 
    if l1[0] < l2[0]: 
        return merge_sorted_lists(l1[1:], l2, merged_list + [l1[0]])
    return merge_sorted_lists(l1, l2[1:], merged_list + [l2[0]])