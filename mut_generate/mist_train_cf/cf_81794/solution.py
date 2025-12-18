"""
QUESTION:
Write a function `minHeap(arr)` to check if the given array represents a min heap. If it does not, the function should convert the array into a min heap and return the number of swaps made. The function should handle arrays of arbitrary length, duplicate values, negative numbers, and zero.
"""

def minHeap(arr):
    def heapify(arr, n, i):
        smallest = i  
        l = 2 * i + 1  # left child
        r = 2 * i + 2  # right child

        if l < n and arr[i] > arr[l]:
            smallest = l

        if r < n and arr[smallest] > arr[r]:
            smallest = r

        if smallest != i:
            arr[i],arr[smallest] = arr[smallest],arr[i] 
            return 1 + heapify(arr, n, smallest)
        return 0

    n = len(arr) 
    swaps = 0
    for i in range(n//2-1, -1, -1):
        swaps += heapify(arr, n, i)
    return swaps