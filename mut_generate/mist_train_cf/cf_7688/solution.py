"""
QUESTION:
Implement a function `mergeSort(arr)` that sorts the input array `arr` in ascending order using a stable sorting algorithm with the following requirements:

- Do not use any built-in sorting functions or algorithms.
- Achieve a time complexity of O(n*log(n)) or better.
- Preserve the relative order of elements with equal values.
- Minimize the use of additional data structures and aim for an in-place sorting algorithm with constant additional memory usage.
- Handle large input sizes efficiently.
- Be adaptive and take advantage of any pre-existing order in the array to improve performance.
"""

def mergeSort(arr):
    """
    Sorts the input array in ascending order using the Merge Sort algorithm.

    Args:
        arr (list): The input array to be sorted.

    Returns:
        list: The sorted array in ascending order.
    """
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)


def merge(left, right):
    """
    Merges two sorted arrays into a single sorted array.

    Args:
        left (list): The first sorted array.
        right (list): The second sorted array.

    Returns:
        list: The merged sorted array.
    """
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result