"""
QUESTION:
Create a function named `convert_to_min_heap(arr)` that takes an array `arr` as input and returns the array converted into a min-heap. The function should have a time complexity of O(N), where N is the size of the array, and a space complexity of O(log N).
"""

def convert_to_min_heap(arr):
    def heapify(arr, n, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] < arr[smallest]:
            smallest = left

        if right < n and arr[right] < arr[smallest]:
            smallest = right

        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            heapify(arr, n, smallest)

    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    return arr