"""
QUESTION:
Implement a function named `heap_sort(arr)` that takes an array of integers `arr` as input and returns the array sorted in descending order without using pre-built Python sorting functions. The array can contain both positive or negative integers, and its size is limited to 1<=n<=10^5 where n is the number of elements in the array. The elements in the array are limited to the range -10^9<=element<=10^9.
"""

def heap_sort(arr):
    """
    Sorts the input array in descending order using heap sort algorithm.

    Args:
    arr (list): A list of integers to be sorted.

    Returns:
    list: The sorted list in descending order.
    """

    def heapify(arr, n, i):
        """
        Builds a heap for a given node 'i'. If the left or right child node's value is greater than the parent node, they swap.

        Args:
        arr (list): The input list.
        n (int): The size of the heap.
        i (int): The index of the node.
        """
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] < arr[left]:
            largest = left
        if right < n and arr[largest] < arr[right]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    # Reverse the array to get the sorted list in descending order
    arr.reverse()
    return arr