"""
QUESTION:
Implement the quick_sort function, which sorts a list of elements using the QuickSort algorithm. The function should take a list of elements as input, partition the list around a pivot element, recursively sort the sublists, and merge the sorted sublists. The function should return the sorted list. The pivot element can be chosen as the middle element of the list. The function should handle lists of any size, including empty lists and lists with a single element.
"""

def quick_sort(arr):
    # Array contains 0 or 1 element
    if len(arr) <= 1:
        return arr
    else:
        # Selects pivot
        pivot = arr[len(arr) // 2]
        # Gather elements less than pivot
        left = [x for x in arr if x < pivot]
        # Gather elements equal to pivot
        middle = [x for x in arr if x == pivot]
        # Gather elements greater than pivot
        right = [x for x in arr if x > pivot]
        # Recursively sort and merge partitions
        return quick_sort(left) + middle + quick_sort(right)