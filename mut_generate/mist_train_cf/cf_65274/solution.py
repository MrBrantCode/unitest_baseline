"""
QUESTION:
Write a Python function named `sort_nested_tuples` that sorts a list of nested tuples based on the second element of each tuple and then rearranges the sorted tuples based on the second last element. The function should take one argument: a list of tuples. Each tuple should have at least two elements.
"""

def sort_nested_tuples(lst):
    lst.sort(key = lambda x: x[1])
    lst.sort(key = lambda x: x[-2])
    return lst