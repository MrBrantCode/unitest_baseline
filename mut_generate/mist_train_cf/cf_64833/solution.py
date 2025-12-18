"""
QUESTION:
Write a function named `convertToMinHeap` that checks if the input array represents a min heap. If not, the function should convert the array into a min heap and return the array along with the number of swaps made to achieve this. The function should be able to handle arrays with duplicate values, negative numbers, and zero.
"""

def convertToMinHeap(arr):
    num_swaps = 0
    def heapify(i, n):
        nonlocal num_swaps
        smallest = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < n and arr[i] > arr[left_child]:
            smallest = left_child

        if right_child < n and arr[smallest] > arr[right_child]:
            smallest = right_child

        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            num_swaps += 1
            num_swaps += heapify(smallest, n)

        return num_swaps

    for i in range((len(arr)-2)//2, -1, -1):
        heapify(i, len(arr))

    return arr, num_swaps