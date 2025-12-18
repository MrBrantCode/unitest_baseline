"""
QUESTION:
Implement a function `odd_even_sort` that takes an array of integers as input and returns the sorted array using the Odd-Even Sort algorithm. The function should handle arrays of any length, including arrays with duplicate elements, negative numbers, and floating-point numbers. It should have a time complexity of O(n log n), where n is the length of the input array. The implementation should be recursive and include a helper function `merge` to merge the sorted odd and even halves of the array.
"""

def odd_even_sort(arr):
    # Check for base case: if the array has only one element, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves: odd-indexed elements and even-indexed elements
    odd_arr = arr[1::2]
    even_arr = arr[::2]
    
    # Recursively sort the odd and even halves
    odd_arr = odd_even_sort(odd_arr)
    even_arr = odd_even_sort(even_arr)
    
    # Merge the sorted odd and even halves
    return merge(odd_arr, even_arr)

def merge(arr1, arr2):
    # Initialize an empty list to store the merged array
    merged = []
    
    # Pointers to track the current index in each array
    i = 0
    j = 0
    
    # Merge the two arrays by comparing elements at corresponding indices
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    
    # Append any remaining elements from the first array
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
    
    # Append any remaining elements from the second array
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
    
    return merged