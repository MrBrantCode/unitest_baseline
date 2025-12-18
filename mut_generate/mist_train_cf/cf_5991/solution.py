"""
QUESTION:
Write a function called `delete_last_occurrence` that takes a list and a value as input and returns a new list where the last occurrence of the specified value is deleted. If the value is not found in the list, return the original list without any modifications. The function must run in O(n) time complexity and O(1) space complexity, where n is the number of elements in the list, and it must not use any built-in functions or methods other than range, len, and del, or any additional data structures such as dictionaries, sets, or arrays.
"""

def delete_last_occurrence(lst, val):
    index = None
    for i in range(len(lst)-1, -1, -1):
        if lst[i] == val:
            index = i
            break
    if index is None:
        return lst
    lst = lst[:]
    del lst[index]
    return lst