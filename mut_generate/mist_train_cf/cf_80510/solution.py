"""
QUESTION:
Implement an interpolationSearch function in Python that takes a list of integers (lst) and an integer (y) as input. The function should return the index of y in lst if present, handling both sorted and unsorted input lists in ascending or descending order. If y is not in lst, the function should return -1. The function should also handle edge cases such as empty or single-element lists. The time complexity should be O(log log n) in the best case and O(n) in the worst case.
"""

def interpolationSearch(lst, y):
    lst.sort()  # Sort the list in ascending order
    low = 0
    high = (len(lst) - 1)

    while low <= high and y >= lst[low] and y <= lst[high]:
        if low == high:
            if lst[low] == y: 
                return low
            return -1
  
        pos = low + ((high - low) // (lst[high] - lst[low]) * (y - lst[low]))
  
        if lst[pos] == y:
            return pos
  
        if lst[pos] < y:
            low = pos + 1
  
        else:
            high = pos - 1
     
    return -1