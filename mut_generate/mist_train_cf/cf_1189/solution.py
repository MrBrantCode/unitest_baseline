"""
QUESTION:
Implement the function bubble_sort(arr, sort_order) to sort the array 'arr' of integers in the specified 'sort_order' ('asc' for ascending or 'desc' for descending). The function should also return the sorted array along with the number of comparisons and swaps made during the sorting process.
"""

def bubble_sort(arr, sort_order):
    n = len(arr)
    comparisons = 0
    swaps = 0

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            comparisons += 1
            if (sort_order == 'asc' and arr[j] > arr[j + 1]) or (sort_order == 'desc' and arr[j] < arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1

    return arr, comparisons, swaps