"""
QUESTION:
Write a function called 'validateUniques' that takes a list as input and returns 'True' if all elements in the list are distinct and 'False' otherwise, without using any external libraries or data structures other than built-in Python data types.
"""

def validateUniques(lst):
    return len(lst) == len(set(lst))