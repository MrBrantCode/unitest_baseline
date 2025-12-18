"""
QUESTION:
Implement a function `bubble_sort(lst)` that sorts a list of distinct integers in ascending order without using built-in sorting functions or algorithms. The function should return a tuple containing the sorted list and the number of swap operations performed.
"""

def bubble_sort(lst):
    n = len(lst)
    swap_count = 0
    for i in range(n-1):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swap_count += 1
    return (lst, swap_count)