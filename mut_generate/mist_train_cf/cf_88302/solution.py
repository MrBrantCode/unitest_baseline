"""
QUESTION:
Write a function `append_sorted(sorted_list, new_element)` that appends a `new_element` to a sorted list `sorted_list` in ascending order while maintaining the list's sorted property. The function should have a time complexity of O(log n) for inserting the `new_element`. Assume that the input `sorted_list` is already sorted in ascending order.
"""

def append_sorted(sorted_list, new_element):
    start = 0
    end = len(sorted_list) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if sorted_list[mid] == new_element:
            return  
        elif sorted_list[mid] < new_element:
            start = mid + 1
        else:
            end = mid - 1

    sorted_list.insert(start, new_element)