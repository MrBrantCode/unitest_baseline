"""
QUESTION:
Create a function called `prod_signs` that takes an array of integers as input. The function should consider only unique, non-zero integers from the array and return the sign of the product of these numbers. The sign should be determined as follows: 1 if the product is positive (i.e., the number of negative numbers is even), and -1 if the product is negative (i.e., the number of negative numbers is odd).
"""

def prod_signs(arr):
    unique_elems = set(x for x in arr if x != 0)
    return 1 if sum(1 for elem in unique_elems if elem < 0) % 2 == 0 else -1