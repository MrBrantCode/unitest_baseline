"""
QUESTION:
Write a function `swap_values` that takes a list `lst` and two values `val1` and `val2` as inputs, swaps all occurrences of `val1` and `val2` in the list, and returns the modified list. The function should handle cases where `val1` and/or `val2` are not present in `lst`, keep the list size constant, and not use built-in Python functions like `replace`.
"""

def swap_values(lst, val1, val2):
    # Temporary placeholder that does not occur in the list
    temp = None
    for i in range(len(lst)):
        if lst[i] == val1:
            lst[i] = temp

    for i in range(len(lst)):
        if lst[i] == val2:
            lst[i] = val1
        elif lst[i] == temp:
            lst[i] = val2
            
    return lst