"""
QUESTION:
Create a function `make_tuples(lst)` that takes a list `lst` as input and returns a new list of tuples, where each tuple contains two consecutive elements from the original list. The function should only include tuples of consecutive elements and should not raise an index error.
"""

def make_tuples(lst):
    return [(lst[i], lst[i+1]) for i in range(len(lst)-1)]