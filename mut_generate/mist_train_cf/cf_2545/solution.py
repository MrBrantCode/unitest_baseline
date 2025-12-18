"""
QUESTION:
Find the kth largest element in an array of unique positive integers without using any built-in sorting or priority queue functions. Implement the algorithm recursively with a time complexity of O(n log k) and a space complexity of O(1), where n is the size of the array. The function should be named `find_kth_largest` and take two parameters: the input array and the value of k.
"""

def find_kth_largest(arr, k):
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

    build_min_heap = lambda: [heapify(arr, k, i) for i in range(k//2 - 1, -1, -1)]

    build_min_heap()

    n = len(arr)
    for i in range(k, n):
        if arr[i] > arr[0]:
            arr[0] = arr[i]
            heapify(arr, k, 0)

    return arr[0]