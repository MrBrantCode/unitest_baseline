"""
QUESTION:
Implement a function named `shell_sort` that sorts an array of integers in ascending order using the Shell sort algorithm. The function should take an array of integers as input, and return the sorted array. The implementation should not use any built-in sorting functions or libraries.
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

        gap //= 2

    return arr