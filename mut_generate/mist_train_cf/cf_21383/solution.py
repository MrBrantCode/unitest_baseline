"""
QUESTION:
Write a recursive function `print_list_reverse` that takes a list (`lst`) and an index as parameters and prints the list from the last element to the first element, without using any built-in functions or methods such as `reverse()`, `[::-1]`, `reversed()`, `list()`, or any form of loop.
"""

def print_list_reverse(lst, index):
    if index < 0:  # Base case: stop when index is negative
        return
    print(lst[index])  # Print the element at the current index
    print_list_reverse(lst, index - 1)  # Recursively call the function with the next index