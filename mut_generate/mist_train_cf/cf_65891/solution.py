"""
QUESTION:
Write a recursive function `print_even(start, end)` that prints even numbers in the range from `start` to `end` without using any loop constructs or libraries. The function should not take any input and only use the given parameters `start` and `end`.
"""

def print_even(start, end):
    if start > end:
        return
    if start % 2 == 0:
        print(start)
        print_even(start + 2, end)
    else:
        print_even(start + 1, end)