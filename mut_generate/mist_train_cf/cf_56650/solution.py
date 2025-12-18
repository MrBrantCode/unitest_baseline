"""
QUESTION:
Create a function `createMinHeap(arr)` that checks if the input array `arr` represents a min heap. If it does, return the original array and 0. If it does not, convert the array into a min heap and return the converted array along with the number of swaps made during the conversion process. The function should be able to handle arrays of arbitrary length, duplicate values, negative numbers, zero, and should be optimized for large inputs. Note that the input array should not contain null values.
"""

def createMinHeap(arr):
    def minHeapify(arr, n, i, swaps):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] > arr[left]:
            smallest = left

        if right < n and arr[smallest] > arr[right]:
            smallest = right

        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            swaps += 1
            swaps = minHeapify(arr, n, smallest, swaps)

        return swaps

    def buildMinHeap(arr):
        swaps = 0
        for i in range(len(arr) // 2 - 1, -1, -1):
            swaps = minHeapify(arr, len(arr), i, swaps)
        return arr, swaps

    def isMinHeap(arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            if 2 * i + 1 < n and arr[i] > arr[2 * i + 1]:
                return False
            if 2 * i + 2 < n and arr[i] > arr[2 * i + 2]:
                return False   
        return True

    if isMinHeap(arr):
        return arr, 0
    else:
        return buildMinHeap(arr)