"""
QUESTION:
Write a function named Multiply that takes a list of integers as input and returns the product of all numbers at even indices in the list that are odd and multiples of 3. The function should start with an initial product of 1.
"""

def Multiply(lst):
    product = 1
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 != 0 and lst[i] % 3 == 0:
            product *= lst[i]
    return product