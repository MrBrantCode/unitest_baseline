"""
QUESTION:
Create a function `will_it_fly` that takes two parameters: `q`, a list of numbers, and `w`, the maximum allowable weight. The function should return `True` if the sum of the elements in `q` is less than or equal to `w` and `q` is a palindrome, and `False` otherwise.
"""

def will_it_fly(q, w):
    # check if the list is palindromic
    if q == q[::-1]:
        # check if the sum of its elements is less than or equal to the upper weight limit
        if sum(q) <= w:
            return True
    return False