"""
QUESTION:
Implement a function named `insertion_sort_descending` that sorts a given array in descending order using the insertion sort algorithm. The function should not modify the original array and should be able to handle arrays of up to 1,000,000 elements. It should not use any built-in sorting functions or libraries. The time complexity of the implementation should be less than O(n^2).
"""

def insertion_sort_descending(arr):
    # Create a copy of the original array
    sorted_arr = arr[:]
    
    # Iterate through the array starting from the second element
    for i in range(1, len(sorted_arr)):
        # Store the current element
        key = sorted_arr[i]
        
        # Move elements of sorted_arr[0..i-1], that are smaller than key,
        # to one position ahead of their current position
        j = i-1
        while j >=0 and key > sorted_arr[j] :
                sorted_arr[j+1] = sorted_arr[j]
                j -= 1
        sorted_arr[j+1] = key

    return sorted_arr