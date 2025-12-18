"""
QUESTION:
Create a function `prodDigits(n)` that calculates the product of the digits in a given integer `n`. The function should multiply all the digits of the number together and return the result as an integer. For example, if `n` is 145, the function should return 20, which is the product of 1, 4, and 5.
"""

def prodDigits(n):
    product = 1
    for d in str(n):
        product *= int(d)
    return product