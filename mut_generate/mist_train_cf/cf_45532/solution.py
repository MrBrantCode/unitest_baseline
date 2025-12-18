"""
QUESTION:
Create a function called `recursive_sum` that takes a list as an argument. The list may contain integers, floats, other lists (which may also contain integers, floats, or other lists), and non-numeric characters. The function should recursively add up all the numbers in the list and ignore non-numeric elements.
"""

def recursive_sum(lst):
    total = 0
    for i in lst:
        if type(i) == list:
            total += recursive_sum(i)
        elif type(i) == int or type(i) == float:
            total += i
    return total