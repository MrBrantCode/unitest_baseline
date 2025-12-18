"""
QUESTION:
Create a function `will_it_fly(q, w)` that takes in two parameters: `q`, a list of numbers, and `w`, a number representing the maximum permissible weight. The function should return `True` if the sum of elements in `q` is less than or equal to `w` and the list is palindromic (symmetrical), and `False` otherwise.
"""

def will_it_fly(q, w):
    return q == q[::-1] and sum(q) <= w