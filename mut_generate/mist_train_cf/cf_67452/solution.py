"""
QUESTION:
Implement the QuickSort algorithm on a doubly linked list to sort its elements in ascending order. The function should be named 'quickSort' and should take a list of integers as input. The list may contain up to 500,000 elements, including duplicates and negative numbers. The function should also track and return the total number of swaps performed during the sorting process.
"""

def quickSort(arr):
    num_of_swaps = [0]
    def partition(arr, low, high):
        i = (low-1)         
        pivot = arr[high]     

        for j in range(low, high):

            if arr[j] <= pivot:
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]
                num_of_swaps[0] += 1

        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i+1)

    def _quickSort(arr, low, high):
        if len(arr) == 1:
            return arr
        if low < high:
            pi = partition(arr, low, high)
            _quickSort(arr, low, pi-1)
            _quickSort(arr, pi+1, high)

    _quickSort(arr, 0, len(arr)-1)
    return arr, num_of_swaps[0]