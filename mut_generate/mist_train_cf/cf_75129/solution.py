"""
QUESTION:
Implement a function named `shell_sort` that takes a list of integers as input, sorts the list using the shell sort algorithm, and returns the sorted list. The function should use a dynamic gap size that starts at half the length of the list and decreases by half with each iteration until it reaches zero.
"""

def shell_sort(lst):
    gap = len(lst) // 2
    while gap > 0:
        for i in range(gap, len(lst)):
            temp = lst[i]
            j = i
            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = temp
        gap //= 2
    return lst