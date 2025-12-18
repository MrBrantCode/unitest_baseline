"""
QUESTION:
Develop a function called `merge_lists` that takes two lists, `l1` and `l2`, as input and returns a new list where the elements from each list are alternated. The function must remove any duplicate values from the input lists before merging them, while preserving the original order of the elements. If one list is shorter than the other, the remaining elements from the longer list should be appended to the end of the resultant list.
"""

def merge_lists(l1, l2):
    # remove duplicates from lists while preserving order
    l1 = sorted(set(l1), key = l1.index)
    l2 = sorted(set(l2), key = l2.index)
    
    # create a new list to hold the result
    result = []
    
    # loop through the lists
    i = 0
    while i < max(len(l1), len(l2)):
        if i < len(l1):
            result.append(l1[i])
        if i < len(l2):
            result.append(l2[i])
        i += 1
    
    return result