"""
QUESTION:
Implement a binary search function `binary_search` that finds the index of a target element in a sorted list and returns the path traversed during the search. The function should take two parameters: a sorted list `my_list` and the target element `find`. The function should return the index of the target element and the path traversed if the element is found, or a message indicating that the element is not in the list along with the path traversed. The function should use a binary search algorithm and should not modify the original list.
"""

def binary_search(my_list, find):
    left, right = 0, len(my_list) - 1
    path = []
    
    while left <= right:
        mid = (left + right) // 2
        path.append(mid)
        
        if my_list[mid] == find:
            return (mid, path)
        elif my_list[mid] < find:
            left = mid + 1
        else:
            right = mid - 1
    
    return ("Element not in list", path)