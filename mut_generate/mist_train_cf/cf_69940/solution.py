"""
QUESTION:
Write a function `swap_values` that takes a list as input and swaps all occurrences of two given values (3 and 7) within the list and its nested sublists, regardless of the depth level. The function should modify the original list and return it.
"""

def swap_values(lst):
    for i in range(len(lst)):
        if type(lst[i]) == list:
            swap_values(lst[i])
        elif lst[i] == 3:
            lst[i] = 7
        elif lst[i] == 7:
            lst[i] = 3
    return lst