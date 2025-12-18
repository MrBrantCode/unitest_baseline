"""
QUESTION:
Find the minimum element in a sorted array with a time complexity of O(log n) without using any looping constructs or recursion. The array is sorted in non-decreasing order. Implement the function `find_min_element`.
"""

def find_min_element(arr):
    low, high = 0, len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < arr[high]:
            high = mid
        else:
            low = mid + 1
    return arr[low]