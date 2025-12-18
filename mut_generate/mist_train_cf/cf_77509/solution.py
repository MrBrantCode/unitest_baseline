"""
QUESTION:
Write a function `merge_sorted_lists` that merges two sorted lists in ascending order and then reverses the elements. The function should take two lists, `list1` and `list2`, as input, and return the merged and reversed list. The input lists are already sorted in ascending order. The function should not use built-in Python methods for sorting and reversing, but using slicing for reversing is allowed. Note that the function may mutate the original lists.
"""

def merge_sorted_lists(list1, list2):
    result = []
    while list1 and list2:
        if list1[0] < list2[0]:  
            result.append(list1.pop(0))
        else:
            result.append(list2.pop(0))
    result += list1
    result += list2
    
    return result[::-1]  # Reverse the list using slicing