"""
QUESTION:
Create a function `sort_list` that sorts a list of integers in ascending order without using any built-in Python sorting functions. The input list consists of the squared values of the first twenty odd integers. The function should return the sorted list.
"""

def sort_list(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1] :
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst