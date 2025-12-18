"""
QUESTION:
Write a function `print_column` that takes a list of integers as input and prints each element on a new line. You cannot use built-in array manipulation methods (e.g., map, join, toString), loops, or recursion.
"""

def print_column(lst):
    def helper(lst, i):
        if i < len(lst):
            print(lst[i])
            helper(lst, i + 1)
        return

    helper(lst, 0)