"""
QUESTION:
Write a function `sort_tuples` that sorts a list of tuples based on the second item of each tuple, and then by the first item in reverse order when the second items are equal. The function should be efficient for large lists.
"""

def sort_tuples(tuples):
    return sorted(tuples, key=lambda x: (x[1], -x[0]))