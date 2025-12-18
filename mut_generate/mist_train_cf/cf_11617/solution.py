"""
QUESTION:
Write a function `quickselect(arr, k)` that finds the Kth smallest element from a given array of N elements. The function should take an array `arr` and an integer `k` as parameters, where `k` is 1-indexed, and return the Kth smallest element in the array. The function should use a recursive algorithm.
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