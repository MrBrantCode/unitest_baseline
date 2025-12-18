"""
QUESTION:
Create a function `sum_at_index(lst, idx)` that takes a list of integer lists `lst` and a position index `idx` as parameters. The function should return a new list containing the sum of integers at the given position index in each sublist. If a sublist does not have enough elements, treat the missing value as zero.
"""

def sum_at_index(lst, idx):
    return [sublist[idx] if idx < len(sublist) else 0 for sublist in lst]