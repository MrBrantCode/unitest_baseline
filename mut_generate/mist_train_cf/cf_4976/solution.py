"""
QUESTION:
Write a function named `binary_search` that performs a recursive binary search to find the first occurrence of a target number in a sorted list of integers. The function should take as input a sorted list `arr`, the target number `target`, and the start and end indices of the current subarray, as well as the number of comparisons made so far. It should return the index of the first occurrence of the target and the total number of comparisons made during the search process.

The function should have a time complexity of O(log n) and a space complexity of O(log n), where n is the size of the input data. It should handle large input data sets efficiently and correctly handle negative numbers and duplicate elements in the input data. If the target is not found, the function should return -1 as the index.
"""

def binary_search(arr, target, start, end, comparisons):
    if start > end:
        return -1, comparisons
    
    mid = start + (end - start) // 2
    
    if arr[mid] == target:
        first_occurrence = mid
        while first_occurrence > 0 and arr[first_occurrence - 1] == target:
            first_occurrence -= 1
        return first_occurrence, comparisons
    
    if arr[mid] > target:
        return binary_search(arr, target, start, mid - 1, comparisons + 1)
    
    return binary_search(arr, target, mid + 1, end, comparisons + 1)