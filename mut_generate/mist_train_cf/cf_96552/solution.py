"""
QUESTION:
Write a function named `print_list_reverse` that prints a list in reverse order without using any built-in functions or methods such as `reverse()`, `[::-1]`, `reversed()`, `list()`, or any form of loop. The function should take a list and an index as parameters.
"""

def entrance(lst, index):
    if index < 0:  
        return
    print(lst[index])  
    entrance(lst, index - 1)  