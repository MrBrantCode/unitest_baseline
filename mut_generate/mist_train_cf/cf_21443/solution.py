"""
QUESTION:
Implement a function named `shell_sort` that takes a list of integers `arr` as input and returns the sorted list using the Shell Sort algorithm. The function should sort the list in ascending order and should be an in-place sorting algorithm (i.e., it should not require any extra space apart from the input array).
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