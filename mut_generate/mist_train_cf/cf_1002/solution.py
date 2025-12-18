"""
QUESTION:
Implement a function `remove_duplicates(arr)` that removes duplicates from a given array of integers in O(n) time complexity and O(1) space complexity. The input array is not empty and can have duplicates. The output should be the modified array with duplicates removed, maintaining the order of the remaining elements, and sorted in non-decreasing order. You cannot use built-in functions or data structures, sorting algorithms, or allocate extra space. The function should sort the array in-place without using any sorting functions.
"""

def remove_duplicates(arr):
    # Implement your own sorting algorithm here
    # For example, you can use bubble sort or insertion sort
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    # Remove duplicates
    write_index = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            arr[write_index] = arr[i]
            write_index += 1
    
    # Return the new array without duplicates
    return arr[:write_index]