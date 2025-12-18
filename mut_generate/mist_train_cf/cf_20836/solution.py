"""
QUESTION:
Write a function named `replace_numbers` that takes a list of integers as input, replaces even numbers with their square and odd numbers with their cube, rounds each result to the nearest whole number, and returns the modified list. The input list can contain up to 10^7 elements.
"""

def replace_numbers(lst):
    for i in range(len(lst)):
        if lst[i] % 2 == 0:  
            lst[i] = round(lst[i] ** 2)
        else:  
            lst[i] = round(lst[i] ** 3)
    return lst