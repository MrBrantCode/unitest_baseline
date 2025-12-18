"""
QUESTION:
Write a function "foo" that takes a dictionary and a list of integers as arguments, sorts the list in descending order, and has a time complexity of O(n^2). What is the minimum number of arguments required for this function?
"""

def foo(dictionary, lst):
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst