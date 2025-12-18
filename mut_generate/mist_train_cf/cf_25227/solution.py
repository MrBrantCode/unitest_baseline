"""
QUESTION:
Write a function named `reverse_print_array` that takes an array as input and prints its elements in reverse order using recursion.
"""

def reverse_print_array(arr):
    if len(arr) == 0:
        return
    reverse_print_array(arr[1:])
    print(arr[0])