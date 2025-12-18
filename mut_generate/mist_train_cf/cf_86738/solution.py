"""
QUESTION:
Create a function named `remove_items` that takes a list `lst` and an item as input. The function should remove all occurrences of the given item from the list without using the built-in 'remove', 'del', or any other built-in functions specifically designed for removing elements from a list, and should have a time complexity of O(n).
"""

def remove_items(lst, item):
    i = 0
    while i < len(lst):
        if lst[i] == item:
            for j in range(i, len(lst) - 1):
                lst[j] = lst[j + 1]
            lst.pop()
        else:
            i += 1
    return lst