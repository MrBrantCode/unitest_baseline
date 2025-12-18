"""
QUESTION:
Write a function named `reverse_list` that takes a Python list as input and returns its reversed version. The function should not use the built-in `reverse()` method, slicing syntax, or any other built-in function or method to reverse the list. Additionally, the function should not use any additional data structures or create any helper functions.
"""

def reverse_list(lst):
    length = len(lst)
    for i in range(length // 2):
        lst[i], lst[length - i - 1] = lst[length - i - 1], lst[i]
    return lst