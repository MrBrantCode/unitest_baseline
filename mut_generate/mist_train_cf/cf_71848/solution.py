"""
QUESTION:
Write a function `quicksort_space_complexity` that explains the space complexity of the quicksort algorithm when it is implemented in-place, and discuss how different pivot selection strategies affect this complexity. Assume the input array has `n` elements.
"""

def quicksort_space_complexity(arr):
    """
    This function explains the space complexity of the quicksort algorithm when it is implemented in-place.
    """
    def _quicksort(arr, low, high):
        if low < high:
            pi = _partition(arr, low, high)
            _quicksort(arr, low, pi - 1)
            _quicksort(arr, pi + 1, high)

    def _partition(arr, low, high):
        pivot = arr[high]
        i = (low - 1)
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return (i + 1)

    _quicksort(arr, 0, len(arr) - 1)