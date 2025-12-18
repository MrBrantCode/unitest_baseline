"""
QUESTION:
Write a function named `print_list_reverse` that takes a list as input and prints its elements in reverse order without using any built-in functions or methods such as `reverse()`, `[::-1]`, `reversed()`, `list()` or any form of loop.
"""

def entrance(lst):
    # Base case: if the list is empty, return
    if not lst:
        return

    # Recursive case: print the last element and call the function again with the list excluding the last element
    print(lst[-1])
    entrance(lst[:-1])