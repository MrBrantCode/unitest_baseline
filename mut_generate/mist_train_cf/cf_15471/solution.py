"""
QUESTION:
Create a function named `find_occurrences` that takes a list `lst` and a number `num` as input and returns a tuple containing the index of the first occurrence and the index of the last occurrence of `num` in `lst`. If `num` is not present in `lst`, the function should return (-1, -1).
"""

def find_occurrences(lst, num):
    try:
        first_index = lst.index(num)
        last_index = len(lst) - lst[::-1].index(num) - 1
        return first_index, last_index
    except ValueError:
        return -1, -1