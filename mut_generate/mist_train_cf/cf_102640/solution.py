"""
QUESTION:
Write a function called `find_index` that takes two parameters: a list `lst` and a number `num`. The function should return the index of the first occurrence of `num` in `lst` if it exists. If `num` is not present in `lst`, the function should return `-1`.
"""

def find_index(lst, num):
    try:
        return lst.index(num)
    except ValueError:
        return -1