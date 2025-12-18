"""
QUESTION:
Write a function `multiply(lst)` that takes a list of integers `lst` as input, identifies the odd numerals at even positions that are multiples of 3, and returns their product.
"""

def multiply(lst):
    product = 1
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 != 0 and lst[i] % 3 == 0:
            product *= lst[i]
    return product