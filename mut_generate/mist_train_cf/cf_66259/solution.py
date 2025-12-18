"""
QUESTION:
Implement the `quickSort` function, which takes an array of integers and sorts it using the QuickSort algorithm with a space complexity of O(log n). The function should not use any built-in sorting functions. It should be efficient for large data sets.
"""

def quickSort(array):
    def partition(array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

    def _quickSort(array, low, high):
        if low < high:
            pi = partition(array, low, high)
            _quickSort(array, low, pi - 1)
            _quickSort(array, pi + 1, high)

    _quickSort(array, 0, len(array) - 1)
    return array