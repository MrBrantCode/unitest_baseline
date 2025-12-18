"""
QUESTION:
Write a function named `find_index` that takes two parameters: a list `arr` and a value `val`. The function should return the sum of all indices at which `val` appears in `arr`. If `val` is not found in `arr`, return -1.
"""

def find_index(arr, val):
    index = 0
    found = False
    for i, num in enumerate(arr):
        if num == val:
            index += i
            found = True
    return index if found else -1