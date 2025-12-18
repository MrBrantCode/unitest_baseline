"""
QUESTION:
Write a function named `merged_list` that takes two lists of integers, `list1` and `list2`, as input. The function should merge these two lists into one, removing any duplicate entries and sorting the resultant list in descending order. The function should not use Python's built-in `merge` or `sorting` functions. The function should return the merged and sorted list of unique elements from both input lists.
"""

def entance(list1: list, list2: list):
    # list to store the merged elements
    merged = []
 
    # iterate through the first list
    for i in list1:
        # add the element if it is not already in the merged list
        if i not in merged:
            merged.append(i)
 
    # iterate through the second list
    for i in list2:
        # add the element if it is not already in the merged list
        if i not in merged:
            merged.append(i)
 
    # length of the merged list
    n = len(merged)
 
    # sort the merged list in descending order
    for i in range(n):
        for j in range(0, n - i - 1):
            # swap if the element found is smaller than the next element
            if merged[j] < merged[j+1]:
                merged[j], merged[j+1] = merged[j+1], merged[j]
 
    return merged