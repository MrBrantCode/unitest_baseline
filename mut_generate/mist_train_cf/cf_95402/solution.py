"""
QUESTION:
Implement the `append_element(lst, element)` function to insert a given element into a sorted list `lst` while maintaining the sorted order. The function should have a time complexity of O(log n) for the insertion operation. The list `lst` is guaranteed to be sorted in ascending order, and the function should return the modified list with the element inserted at the correct position.
"""

def insert_element(lst, element):
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