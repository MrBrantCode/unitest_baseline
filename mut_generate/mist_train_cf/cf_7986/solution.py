"""
QUESTION:
Create a function `reverse_print_odd` that takes an array of strings as input, prints the elements with an odd number of characters in reverse order, and handles any invalid inputs or unexpected errors that may occur during execution.
"""

def reverse_print_odd(arr):
    if len(arr) == 0:
        return

    if len(arr[-1]) % 2 != 0:
        print(arr[-1])

    reverse_print_odd(arr[:-1])