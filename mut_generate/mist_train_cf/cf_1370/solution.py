"""
QUESTION:
Implement a function called `shell_sort` that sorts an array of integers in ascending order using the shell sort algorithm with a time complexity of O(n^2). The implementation should be in-place, handle duplicate elements, and use Knuth's sequence for the gap values. The function should take an array of integers as input and return the sorted array.
"""

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap = gap // 2
    return arr