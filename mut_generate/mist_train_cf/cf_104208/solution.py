"""
QUESTION:
Create a function named `print_reverse` that takes a list of integers as input and prints the elements in reverse order using recursion. The function should not return any value, only print the elements.
"""

def print_reverse(arr):
    if len(arr) == 0:
        return
    else:
        print(arr[-1])
        print_reverse(arr[:-1])