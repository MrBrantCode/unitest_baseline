"""
QUESTION:
Create a function named `multiply_tuple_and_append` that takes two parameters: a tuple of numbers and a list. The function should multiply all the numbers in the tuple together and append the result to the list. The function should then return the updated list. The input list should be modified in-place.
"""

def multiply_tuple_and_append(tup, lst):
    product = 1
    for x in tup:
        product *= x
    lst.append(product)
    return lst