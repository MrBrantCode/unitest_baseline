"""
QUESTION:
Create a function called `kthSmallest` that takes a sorted array of integers and an integer `k` as input, and returns the kth smallest element in the array. The array may contain duplicate elements. The function should be optimized for efficiency, and the indexing should start from 1 (i.e., the smallest element is at the 1st position, not the 0th position). If `k` is less than or equal to 0, or greater than the size of the array, the function should return `None`.
"""

def kthSmallest(arr, k): 
    """
    Returns the kth smallest element in a sorted array.

    Args:
        arr (list): A sorted array of integers.
        k (int): The position of the element to return.

    Returns:
        int or None: The kth smallest element if k is within bounds, otherwise None.
    """
    # If k is smaller than 0 or larger than array size
    if (k <= 0 or k > len(arr)): 
        return None
  
    return arr[k-1]