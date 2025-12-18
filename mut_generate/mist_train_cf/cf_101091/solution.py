"""
QUESTION:
Create a function named `reverse_int_list` that takes a list as input, reverses the order of the integer elements, and returns the result while excluding non-integer elements. If the input list contains no integers, the function should return an empty list. The time complexity of the function should be O(n/2).
"""

def reverse_int_list(lst):
    int_lst = [x for x in lst if isinstance(x, int)]
    if not int_lst:
        return []
    n = len(int_lst)
    for i in range(n // 2):
        int_lst[i], int_lst[n - i - 1] = int_lst[n - i - 1], int_lst[i]
    return int_lst