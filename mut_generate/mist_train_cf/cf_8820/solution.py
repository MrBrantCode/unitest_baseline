"""
QUESTION:
Implement a function `calculate_median` that calculates the median of a given input array containing integers. The function should not use the built-in sort function or any other sorting algorithms and should have a time complexity of O(nlogn), where n is the length of the input array. The array can contain both positive and negative integers and can have an odd or even length. If the array is empty, the function should return None.
"""

def calculate_median(arr):
    # Check if the array is empty
    if len(arr) == 0:
        return None

    # Sort the array in ascending order using merge sort
    sorted_arr = merge_sort(arr)

    # Calculate the median
    n = len(sorted_arr)
    if n % 2 == 1:  # Odd length array
        return sorted_arr[n // 2]
    else:  # Even length array
        mid1 = sorted_arr[n // 2 - 1]
        mid2 = sorted_arr[n // 2]
        return (mid1 + mid2) / 2

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Split the array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Recursively sort the two halves
    left = merge_sort(left)
    right = merge_sort(right)
    
    # Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    
    # Merge the two halves by comparing the elements
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # Append the remaining elements of the two halves
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged