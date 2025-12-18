"""
QUESTION:
Write a function `append_to_lists` that takes a string input containing two comma-separated values, appends the first value to list A and the second value to list B, and returns a dictionary with the elements of list A as keys and the corresponding elements of list B as values. Lists A and B should be defined outside the function and initialized as empty lists.
"""

def append_to_lists(string_input):
    string_list = string_input.split(',')
    A.append(string_list[0])
    B.append(string_list[1])
    dictionary = dict(zip(A, B))
    return dictionary