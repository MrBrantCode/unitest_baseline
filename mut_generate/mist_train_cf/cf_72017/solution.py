"""
QUESTION:
Create a function called `reverse_lexi` that takes a list of strings as input, removes duplicate strings, sorts the remaining strings in lexicographical order, and returns them in reverse order. The function should not use built-in sorting functions such as `sort()` or `reverse()`, nor should it use the `set()` function to remove duplicates.
"""

def reverse_lexi(lst):
    # remove duplicates
    unique_lst = []
    for i in lst:
        if i not in unique_lst:
            unique_lst.append(i)

    # bubble sort for lexicographical order
    for i in range(len(unique_lst)):
        for j in range(i + 1, len(unique_lst)):
            if unique_lst[i] > unique_lst[j]:
                unique_lst[i], unique_lst[j] = unique_lst[j], unique_lst[i]

    # reverse list
    reversed_lst = []
    for i in unique_lst:
        reversed_lst.insert(0, i)

    return reversed_lst