"""
QUESTION:
Write a function `remove_duplicates` that takes an array of integers as input and returns a new array with duplicates removed. The function should not use any built-in functions or data structures, and should maintain the order of the remaining elements. The function should also sort the array in non-decreasing order without using any sorting algorithms or built-in sorting functions. The time complexity should be O(n) and the space complexity should be O(1).
"""

def remove_duplicates(arr):
    # Implement your own sorting algorithm here
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    write_index = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            arr[write_index] = arr[i]
            write_index += 1
    
    return arr[:write_index]