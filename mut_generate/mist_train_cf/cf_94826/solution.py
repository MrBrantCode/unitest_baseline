"""
QUESTION:
Write a function named `square_list` that takes a list of elements as input, squares each integer element, and returns a new list containing the squared integer elements. The function should ignore non-integer elements and handle empty lists.
"""

def square_list(lst):
    result = []
    for element in lst:
        if isinstance(element, int):
            result.append(element ** 2)
    return result