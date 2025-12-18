"""
QUESTION:
Write a recursive function `print_num(i, limit)` that prints integers from `i` up to but not including `limit`, using recursive calls without any loop constructs. The function should include error checking to prevent infinite recursion.
"""

def print_num(i, limit):
    # Error checking to prevent infinite recursion
    if i >= limit:
        return
    else:
        print(i)
        print_num(i + 1, limit)  # Recursive call