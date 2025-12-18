"""
QUESTION:
Implement a function named `shell_sort` that takes a list of integers as input and returns the sorted list without using any built-in sorting functions or libraries. The function should use the Shell sort algorithm to sort the input list in ascending order.
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