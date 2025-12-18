"""
QUESTION:
Create a function `product_of_every_third` that takes a list of integers as input and returns the product of every third element in the list. The function should use 0-based indexing and consider the first element as the first element (index 0).
"""

def product_of_every_third(arr):
    product = 1
    for num in arr[::3]:
        product *= num
    return product