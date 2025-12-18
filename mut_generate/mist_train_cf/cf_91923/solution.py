"""
QUESTION:
Write a function named `quickselect(arr, k)` that takes an array of integers `arr` and an integer `k` as parameters, and returns the kth smallest element from the array using a recursive algorithm. The function should partition the array around a pivot and recursively search for the kth smallest element in the appropriate partition.
"""

def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    
    pivot = arr[len(arr) // 2]
    smaller_elements = [x for x in arr if x < pivot]
    larger_elements = [x for x in arr if x > pivot]
    equal_elements = [x for x in arr if x == pivot]
    
    if k <= len(smaller_elements):
        return quickselect(smaller_elements, k)
    elif k > len(smaller_elements) + len(equal_elements):
        return quickselect(larger_elements, k - len(smaller_elements) - len(equal_elements))
    else:
        return equal_elements[0]