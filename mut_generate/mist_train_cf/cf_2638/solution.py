"""
QUESTION:
Create a function named `search_list` that takes two parameters: a sorted list `l` containing integers and a value `v` to be searched in the list. The function should return the index of the first occurrence of `v` in `l` if found, and -1 otherwise. The function should have a time complexity of O(log n) and should handle cases where `v` is of a different type than the elements in `l`.
"""

def search_list(l, v):
    # Check if the list l is empty
    if not l:
        return -1
    
    # Check if the value v is of a different type than the elements in l
    if isinstance(v, type(l[0])) is False:
        return -1
    
    # Perform binary search on the sorted list l
    low = 0
    high = len(l) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if l[mid] == v:
            # Check if the found value is the first occurrence
            if mid == 0 or l[mid - 1] != v:
                return mid
            else:
                high = mid - 1
        elif l[mid] < v:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1