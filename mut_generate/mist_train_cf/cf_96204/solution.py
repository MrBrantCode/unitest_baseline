"""
QUESTION:
Write a function called `delete_last_occurrence(lst, value)` that takes a list `lst` and a value as input, and returns the modified list after deleting the last occurrence of the specified value. The function should not use any built-in functions or methods, such as `remove()` or `index()`, and should not use additional data structures like dictionaries or sets. The function should have a time complexity of O(n), where n is the number of elements in the list. If the value is not found in the list, the function should return the original list unchanged.
"""

def delete_last_occurrence(lst, value):
    last_index = -1
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == value:
            last_index = i
            break

    if last_index != -1:
        del lst[last_index]

    return lst