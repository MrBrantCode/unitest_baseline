"""
QUESTION:
Design a function `findFirstLastOccurrence` that takes a sorted array of integers and a target number `k` as input. The function should return a tuple containing the indices of the first and last occurrence of `k` in the array. If `k` does not exist in the array, the function should return a tuple of two -1 values. The function should use a binary search approach to achieve this.
"""

def findFirstLastOccurrence(arr, k):
    """
    Returns a tuple containing the indices of the first and last occurrence of k in the array.
    
    Args:
        arr (list): A sorted array of integers.
        k (int): The target number.
    
    Returns:
        tuple: A tuple containing the indices of the first and last occurrence of k. If k does not exist in the array, returns (-1, -1).
    """

    # Find the first occurrence
    left, right = 0, len(arr) - 1
    first_occurrence = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == k and (mid == 0 or arr[mid-1] < k):
            first_occurrence = mid
            break
        elif arr[mid] < k:
            left = mid + 1
        else:
            right = mid - 1

    # Find the last occurrence
    left, right = 0, len(arr) - 1
    last_occurrence = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == k and (mid == len(arr) - 1 or arr[mid+1] > k):
            last_occurrence = mid
            break
        elif arr[mid] > k:
            right = mid - 1
        else:
            left = mid + 1
    
    return first_occurrence, last_occurrence