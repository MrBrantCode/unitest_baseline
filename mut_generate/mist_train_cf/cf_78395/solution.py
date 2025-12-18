"""
QUESTION:
Implement a function named `median` that takes two parameters: a list `lst` containing integers or tuples, and a custom comparison function `cmp_func`. The function should calculate the median of the list without sorting the list using built-in functions like `sorted()` or `numpy.sort()`, but it can use the list's `sort()` method for in-place sorting. The function should handle lists with both even and odd lengths, as well as duplicates. The `cmp_func` should be used to compare elements in the list, particularly when the list contains tuples.
"""

def median(lst, cmp_func):
    """Compute and return the median from an unsorted list or list of tuples without using built-in functions.
    Handles duplicates, lists with both even and odd length, and utilizes cmp_func for comparisons."""
    try:
        lst.sort(key=cmp_func)  # sort in-place using the custom comparison function
    except TypeError:
        print("cmp_func must be a function that takes one argument and returns a key to sort the list.")
        return None

    len_lst = len(lst)

    # handle odd-length lst
    if len_lst % 2 == 1:
        return lst[len_lst // 2]
    # handle even-length lst
    else:
        i = len_lst // 2
        return (lst[i - 1] + lst[i]) / 2