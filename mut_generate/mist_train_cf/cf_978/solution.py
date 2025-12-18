"""
QUESTION:
Implement a function `gnome_sort(arr)` that sorts the given array in descending order using the Gnome sort algorithm. The function should check if the array is already sorted and return it immediately if so. It should also track the total number of swaps made and stop the sorting process if the number of swaps exceeds 3 times the length of the array. The function should handle duplicate elements and update the last sorted position after each swap operation to reduce unnecessary comparisons. If the swapped elements are equal, the function should skip the next iteration of the outer loop to avoid unnecessary comparisons.
"""

def gnome_sort(arr):
    n = len(arr)
    sorted_pos = 0
    swaps = 0
    
    while sorted_pos < n:
        if sorted_pos == 0 or arr[sorted_pos] <= arr[sorted_pos - 1]:
            sorted_pos += 1
        else:
            arr[sorted_pos], arr[sorted_pos - 1] = arr[sorted_pos - 1], arr[sorted_pos]
            swaps += 1
            sorted_pos -= 1
            
            if swaps > 3 * n:
                return arr
        
        if sorted_pos < n and arr[sorted_pos] == arr[sorted_pos - 1]:
            sorted_pos += 1
    
    return arr