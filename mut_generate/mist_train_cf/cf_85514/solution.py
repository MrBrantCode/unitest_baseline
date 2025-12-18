"""
QUESTION:
Develop a function named `sum_nested` that takes a list of integers as input. The list can contain nested sublists up to three levels deep. The function should return the cumulative sum of all integers present within the list and its nested sublists.
"""

def sum_nested(lst):
    total = 0
    for i in lst:
        if type(i) is list:
            total += sum_nested(i)
        else:
            total += i
    return total