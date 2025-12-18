"""
QUESTION:
Create a function sum_list_elements that takes a list of numbers as input and returns the sum of all elements in the list. The function should not use any built-in sum functions.
"""

def sum_list_elements(lst):
    result = 0
    for i in lst:
        result += i
    return result