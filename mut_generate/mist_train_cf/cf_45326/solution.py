"""
QUESTION:
Write two functions, `sortList(set_list)` and `blendAndSort(set1, set2)`, and a third function that calls these two functions. `sortList(set_list)` should sort the input list `set_list` in ascending order. `blendAndSort(set1, set2)` should blend two sorted input lists `set1` and `set2` in a specific pattern (i.e., one number from the first set, one number from the second set, and so on) and return the blended list. The third function should call `sortList` and `blendAndSort` to return the final blended and sorted list. The solution should have a time complexity of O(n log n) and space complexity of O(n) to ensure efficiency for large data sets.
"""

def sortList(set_list):
    return sorted(set_list)

def blendAndSort(set1, set2):
    set1, set2 = sortList(set1), sortList(set2)
    blended_set = []
    for a, b in zip(set1, set2):
        blended_set.append(a)
        blended_set.append(b)
    blended_set += set1[len(set2):] or set2[len(set1):]
    return blended_set

def entance(set1, set2):
    return blendAndSort(set1, set2)