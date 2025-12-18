"""
QUESTION:
Implement a function named `merge_sort` that takes an array as input and returns the sorted array using the merge sort algorithm without recursion. The function should have a time complexity of O(n log n) and a space complexity of O(n).
"""

def merge_sort(arr):
    n = len(arr)
    
    # Create a temporary array to store the sorted sublists
    temp_arr = [0] * n
    
    # Divide the list into sublists of size 1, then merge them back together
    sublist_size = 1
    while sublist_size < n:
        left = 0
        while left < n - 1:
            # Find the mid and right indices for merging
            mid = min(left + sublist_size - 1, n - 1)
            right = min(left + 2 * sublist_size - 1, n - 1)
            
            # Merge the sublists
            merge(arr, temp_arr, left, mid, right)
            
            # Move to the next pair of sublists
            left += 2 * sublist_size
        
        # Double the size of sublists for the next iteration
        sublist_size *= 2
    
    return arr


def merge(arr, temp_arr, left, mid, right):
    # Copy the elements from arr to temp_arr
    for i in range(left, right + 1):
        temp_arr[i] = arr[i]
    
    # Merge the sublists from temp_arr back to arr
    i = left
    j = mid + 1
    k = left
    
    while i <= mid and j <= right:
        if temp_arr[i] <= temp_arr[j]:
            arr[k] = temp_arr[i]
            i += 1
        else:
            arr[k] = temp_arr[j]
            j += 1
        k += 1
    
    # Copy the remaining elements from the left sublist
    while i <= mid:
        arr[k] = temp_arr[i]
        i += 1
        k += 1
    
    # Copy the remaining elements from the right sublist
    while j <= right:
        arr[k] = temp_arr[j]
        j += 1
        k += 1