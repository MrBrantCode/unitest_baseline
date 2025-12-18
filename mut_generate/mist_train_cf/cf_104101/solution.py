"""
QUESTION:
Implement a function called `reverse_list` that takes a list as input and reverses its order. The function should only use basic operations and control flow statements, and it must have a time complexity of O(n), where n is the length of the input list. The function cannot use built-in functions or methods that directly reverse a list, such as `reverse()` or slicing with negative steps.
"""

def reverse_list(lst):
    n = len(lst)
    for i in range(n // 2):
        lst[i], lst[n-i-1] = lst[n-i-1], lst[i]
    return lst