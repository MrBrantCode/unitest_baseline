"""
QUESTION:
Write a function `find_unique_length` that takes two strings `a` and `b` as input, and returns the length of the unique substring sequence not shared by these two strings. The function should consider unique characters only and exclude duplicates.
"""

def find_unique_length(a, b):
    set_a = set(a)
    set_b = set(b)

    unique_a = set_a - set_b
    unique_b = set_b - set_a

    return len(unique_a | unique_b)