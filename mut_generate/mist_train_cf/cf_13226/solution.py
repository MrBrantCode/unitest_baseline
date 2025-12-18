"""
QUESTION:
Construct a function `binary_search` to check whether a given element is present in a sorted array. The array is guaranteed to be sorted in ascending order. The function should return True if the element is present, False otherwise. The time complexity of the solution should be O(log n), where n is the size of the array.
"""

def binary_search(arr, element):
    """
    Searches for a given element in a sorted array using binary search.
    
    Args:
        arr (list): A sorted list of elements.
        element: The element to be searched.
    
    Returns:
        bool: True if the element is present, False otherwise.
    """
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == element:
            return True
        elif arr[mid] < element:
            start = mid + 1
        else:
            end = mid - 1
    
    return False