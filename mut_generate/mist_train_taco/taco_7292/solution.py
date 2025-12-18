"""
QUESTION:
Write a function `reverse` which reverses a list (or in clojure's case, any list-like data structure)

(the dedicated builtin(s) functionalities are deactivated)
"""

from collections import deque

def reverse_list(lst):
    """
    Reverses a list (or list-like data structure).

    Parameters:
    lst (list): The input list to be reversed.

    Returns:
    list: A new list that is the reverse of the input list.
    """
    q = deque()
    for x in lst:
        q.appendleft(x)
    return list(q)