"""
QUESTION:
Write a recursive function `merge_sort` that sorts an array of integers in descending order and keeps track of the number of swaps made during the sorting process. The function should handle arrays with duplicate elements by sorting them in descending order and rearranging the duplicates in ascending order within their respective groups. The function should return a tuple containing the sorted array and the number of swaps.
"""

def merge_sort(arr):
    # Base case: if the array contains 0 or 1 element, it is already sorted
    if len(arr) <= 1:
        return arr, 0
    
    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort the two halves and keep track of the number of swaps
    left_sorted, left_swaps = merge_sort(left_half)
    right_sorted, right_swaps = merge_sort(right_half)
    
    # Merge the two sorted halves
    sorted_arr = []
    swaps = left_swaps + right_swaps
    i, j = 0, 0
    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] >= right_sorted[j]:
            sorted_arr.append(left_sorted[i])
            i += 1
        else:
            sorted_arr.append(right_sorted[j])
            j += 1
            swaps += len(left_sorted) - i  # Count the number of swaps made
            
    # Append any remaining elements from the left half
    sorted_arr.extend(left_sorted[i:])
    
    # Append any remaining elements from the right half
    sorted_arr.extend(right_sorted[j:])
    
    return sorted_arr, swaps