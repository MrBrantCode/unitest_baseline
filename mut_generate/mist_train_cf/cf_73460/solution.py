"""
QUESTION:
Implement an in-place sorting algorithm that sorts an array of integers in either ascending or descending order based on user input. The function should return the sorted array, the count of total comparisons, and the count of swaps made during the process. The function should be efficient in terms of time complexity and minimize the use of additional space, without using Python's inbuilt sorting functions.

The function should be named `sort(arr, ascending=True)` where `arr` is the input array of integers and `ascending` is a boolean parameter that defaults to `True` for ascending order and can be set to `False` for descending order.
"""

def sort(arr, ascending=True):
    def quicksort(arr, start, end, ascending):
        if start < end:
            pi, comparison, swap = partition(arr, start, end, ascending)
            lc, ls = quicksort(arr, start, pi - 1, ascending)
            rc, rs = quicksort(arr, pi + 1, end, ascending)
            return (comparison + lc + rc, swap + ls + rs)
        else:
            return 0, 0

    def partition(arr, start, end, ascending):
        i = (start - 1)
        pivot = arr[end]
        comparison = 0
        swap = 0
        for j in range(start, end):
            comparison += 1
            if (arr[j] <= pivot and ascending) or (arr[j] >= pivot and not ascending):
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
                swap += 1
        arr[i+1], arr[end] = arr[end], arr[i+1]
        return (i + 1, comparison, swap + 1)

    n = len(arr)
    c, s = quicksort(arr, 0, n - 1, ascending)
    return arr, c, s