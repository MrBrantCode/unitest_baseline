"""
QUESTION:
Create a function search_list(l, v) that searches a sorted list l for the value v. The list l can contain both positive and negative integers and can have duplicate values. The function should return the index of the first occurrence of v if found, or -1 if v is not found in the list l. The function should be able to handle large lists efficiently, with a time complexity of O(log n) or better. The function should also handle cases where the value v is of a different type than the values in the list l, in which case it should return -1.
"""

def search_list(l, v):
    # Check if the list l is empty
    if not l:
        return -1
    
    # Check if v is a string and the values in the list l are integers
    if isinstance(v, str) and all(isinstance(x, int) for x in l):
        return -1
    
    # Check if v is a list and the values in the list l are integers
    if isinstance(v, list) and all(isinstance(x, int) for x in l):
        return -1
    
    # Check if v is a dictionary and the values in the list l are integers
    if isinstance(v, dict) and all(isinstance(x, int) for x in l):
        return -1
    
    # Check if v is a tuple and the values in the list l are integers
    if isinstance(v, tuple) and all(isinstance(x, int) for x in l):
        return -1
    
    # Check if v is a float and the values in the list l are integers
    if isinstance(v, float) and all(isinstance(x, int) for x in l):
        return -1
    
    # Check if v is None and the values in the list l are integers
    if v is None and all(isinstance(x, int) for x in l):
        return -1
    
    # Check if v is a boolean value and the values in the list l are integers
    if isinstance(v, bool) and all(isinstance(x, int) for x in l):
        return -1
    
    # Check if v is a string and the values in the list l are floats
    if isinstance(v, str) and all(isinstance(x, float) for x in l):
        return -1
    
    # Check if v is a string and the values in the list l are boolean values
    if isinstance(v, str) and all(isinstance(x, bool) for x in l):
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