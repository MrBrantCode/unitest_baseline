"""
QUESTION:
Write a function `get_first_element(lst)` that takes a list of tuples as input, where each tuple contains two integers. The function should return a list of integers where for each tuple, if the first element is odd, it returns the first element; otherwise, it returns the second element.
"""

def get_first_element(lst):
    result = []
    for tup in lst:
        if tup[0] % 2 == 1:
            result.append(tup[0])
        else:
            result.append(tup[1])
    return result