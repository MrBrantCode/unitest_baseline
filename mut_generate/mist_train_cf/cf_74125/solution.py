"""
QUESTION:
Write a function named `common` that takes two lists as input and returns a new list containing the unique common elements of the input lists in sorted order. The function should not use any built-in Python list functions like `set` or `sort`. Instead, implement a custom sorting algorithm and a method to eliminate duplicates.
"""

def custom_sort(lst: list) -> list:
    for i in range(1, len(lst)):
        current = lst[i]
        pos = i
        while pos > 0 and lst[pos - 1] > current:
            lst[pos] = lst[pos - 1]
            pos = pos - 1
        lst[pos] = current
    return lst

def common(l1: list, l2: list) -> list:
    common_list = []
    for i in l1:
        if i in l2:
            common_list.append(i)
            
    unique_common_list = []
    for i in common_list:
        if i not in unique_common_list:
            unique_common_list.append(i)

    return custom_sort(unique_common_list)