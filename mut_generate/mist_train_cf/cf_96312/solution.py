"""
QUESTION:
Write a function `replace_numbers(lst)` that replaces even numbers in the input list `lst` with their square and odd numbers with their cube, with each result rounded to the nearest whole number. The function should modify the input list in-place and return the modified list. The input list can contain up to 10^7 elements.
"""

def replace_numbers(lst):
    for i in range(len(lst)):
        if lst[i] % 2 == 0:  
            lst[i] = round(lst[i] ** 2)
        else:  
            lst[i] = round(lst[i] ** 3)
    return lst