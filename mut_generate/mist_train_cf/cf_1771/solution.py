"""
QUESTION:
Insert a new element into a sorted array without using built-in sorting functions or libraries, maintaining the existing order of elements. The function should have a time complexity of O(log n). 

The function, `insertElement(arr, newElement)`, takes a sorted array `arr` and the new element `newElement` as input, and inserts `newElement` into `arr` at its correct position.
"""

def insertElement(arr, newElement):
    """
    Inserts a new element into a sorted array without using built-in sorting functions or libraries,
    maintaining the existing order of elements.

    Args:
    arr (list): The sorted array.
    newElement: The element to be inserted.

    Returns:
    list: The updated array with the new element inserted at its correct position.
    """
    n = len(arr)
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2
        
        if newElement == arr[mid]:
            arr.insert(mid + 1, newElement)
            return arr
        
        if newElement < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    
    # Shift elements to the right
    arr.insert(start + 1, newElement)
    
    return arr