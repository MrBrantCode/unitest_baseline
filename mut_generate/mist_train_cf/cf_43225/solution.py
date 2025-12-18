"""
QUESTION:
Implement the `shell_sort` function to sort an unsorted list of integers in ascending order using the shell sort algorithm. The function should take a list of integers as input and return the sorted list. The list can contain duplicate elements and is not guaranteed to be of any specific size. The function should not use any built-in sorting functions or libraries.
"""

def shell_sort(alist):
    n = len(alist)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = alist[i]
            j = i
            while j >= gap and alist[j - gap] > temp:
                alist[j] = alist[j - gap]
                j -= gap
            alist[j] = temp
        gap //= 2
    return alist