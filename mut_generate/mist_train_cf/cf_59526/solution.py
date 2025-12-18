"""
QUESTION:
Create a recursive function named `sort_descending` that takes a list of elements as input and returns the sorted list in descending order without using the built-in `sort()` function. The function should be able to handle lists of varying lengths, including empty lists and lists with duplicate elements.
"""

def sort_descending(lst):
    if not lst:
        return []
    if len(lst) == 1:
        return lst
    max_value = max(lst)
    lst.remove(max_value)
    return [max_value] + sort_descending(lst)