"""
QUESTION:
Write a Python function named `reverse_int_list` that takes a list as input, filters out non-integer elements, reverses the order of the remaining integers, and returns them in a new list. The function should have a time complexity of O(n/2) and return an empty list if there are no valid integers in the input list.
"""

def reverse_int_list(lst):
    int_lst = [x for x in lst if isinstance(x, int)]
    if not int_lst:
        return []
    n = len(int_lst)
    for i in range(n // 2):
        int_lst[i], int_lst[n - i - 1] = int_lst[n - i - 1], int_lst[i]
    return int_lst