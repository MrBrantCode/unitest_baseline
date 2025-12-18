"""
QUESTION:
Implement the `insertion_sort` function to sort a list of mixed fractions, including nested lists of fractions. The nested lists should be treated as single units and sorted by their largest fraction. The function should have a time complexity as optimal as possible. The input list can contain both integers and fractions, and the function should return a sorted list in ascending order. The function should handle fractions and nested lists, but it does not need to handle other data types.
"""

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and maxval(lst[j]) > maxval(key):
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst

def maxval(item):
    if isinstance(item, list):
        return max(item, key=lambda x: float(str(x)))
    else:
        return float(str(item))