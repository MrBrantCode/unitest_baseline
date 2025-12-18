"""
QUESTION:
Write a function named `check_array_heap` that takes an array of integers as input. The function should check if the array represents a min heap. If the array does not represent a min heap, the function should convert it into a min heap. The function should handle duplicate values, negative numbers, and zero. The function should return the min heap as an array and the minimum value in the heap. Implement the solution without using any built-in heap functions or libraries.
"""

def check_array_heap(arr):
    def is_heap(arr, n, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[i] > arr[left]:
            smallest = left
        
        if right < n and arr[smallest] > arr[right]:
            smallest = right
        
        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            is_heap(arr, n, smallest)
    
    n = len(arr)
    start_index = n // 2 - 1
    for i in range(start_index, -1, -1):
        is_heap(arr, n, i)
    
    return arr, arr[0]