"""
QUESTION:
Write a function `append_element(lst, element)` that inserts the given `element` into the sorted list `lst` while maintaining the sorted order. The function should have a time complexity of O(log n) for the insertion operation.
"""

def append_element(lst, element):
    start = 0
    end = len(lst) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == element:
            return lst
        elif lst[mid] < element:
            start = mid + 1
        else:
            end = mid - 1
    
    lst.insert(start, element)
    return lst