"""
QUESTION:
Delete the last occurrence of a specified value from a list without using built-in functions or methods, and additional data structures. The function should have a time complexity of O(n), where n is the number of elements in the list, and the function should not modify the list if the value is not found.
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