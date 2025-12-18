"""
QUESTION:
Write a function named `print_list_reverse` that takes a list as input and prints the elements of the list from the last element to the first element. The function should not use any built-in functions or methods such as `reverse()`, `[::-1]`, `reversed()`, `list()`, or any form of loop. The function should be able to handle an empty list as input.
"""

def print_list_reverse(lst):
    # Base case: if the list is empty, return
    if not lst:
        return

    # Recursive case: print the last element and call the function again with the list excluding the last element
    print(lst[-1])
    print_list_reverse(lst[:-1])