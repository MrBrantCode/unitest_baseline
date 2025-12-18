"""
QUESTION:
Create a function named `sort_list` that takes two parameters: a list (`lst`) containing either integers or tuples with at least two elements, and an optional boolean parameter (`ascending`) with a default value of `False`. The function should sort the list in descending order if `ascending` is `False` and in ascending order if `ascending` is `True`. If the list contains tuples, the sorting should be based on the first integer of each tuple. The list can contain up to 10^6 elements, and the integers can range from negative to positive values.
"""

def sort_list(lst, ascending=False):
    if isinstance(lst[0], int):
        lst.sort(reverse=not ascending)
    elif isinstance(lst[0], tuple):
        lst.sort(key=lambda x: x[0], reverse=not ascending)
    return lst