"""
QUESTION:
Create a function named `remove_even` that takes a list as input, removes all even elements from the list, and returns the resulting list of odd elements. The function should also include error handling to return an error message if the input is not a list. The solution should be efficient enough to handle lists of up to one million elements and should not use built-in functions like `filter()` or list comprehensions.
"""

def remove_even(lst):
    if type(lst) is not list:
        return "Error: Input is not a list"
    new_lst = []
    for i in lst:
        if i % 2 != 0:
            new_lst.append(i)
    return new_lst