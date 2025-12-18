"""
QUESTION:
Create a function `transform_list` that takes a list of integers as input. The function should return a new list where each even number in the input list is tripled and each odd number is replaced with its cube root rounded to the nearest integer.
"""

def transform_list(lst):
    new_lst = []
    for num in lst:
        if num % 2 == 0:
            new_lst.append(num * 3)
        else:
            new_lst.append(round(num ** (1/3)))
    return new_lst