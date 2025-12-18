"""
QUESTION:
Implement the `modified_selection_sort` function to sort a given list of numbers in ascending order. This function should also track the total number of swaps, check if swapping two numbers results in three sequential numbers being in ascending order before each swap, and track the position of each number before and after sorting in a separate array. The function should return the sorted array, the total number of swaps, and the position tracking array. The function should be able to handle negative and fractional numbers.
"""

def modified_selection_sort(arr):
    positions = []
    original = arr.copy()
    
    n = len(arr)
    swap_count = 0
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Check the condition before swapping      
        if i > 0 and min_idx != i:
            if arr[i - 1] > arr[min_idx] or arr[i + 1] < arr[min_idx]:
                continue
        
        # Swap the element to the right place and increase the count
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swap_count += 1
        
        # Determining the position
        original_pos = original.index(arr[i])
        positions.append((arr[i], original_pos, i, abs(original_pos - i)))

    return arr, swap_count, positions