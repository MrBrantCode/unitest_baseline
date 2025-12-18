"""
QUESTION:
Write a function named `multiply` that takes a list of integers as input. The function should return the product of the numbers at even indexes in the list that are also multiples of 3. The product should be 1 if no such numbers are found.
"""

def multiply(lst):
    """
    An array of integers is provided, denoted as 'lst'. Calculate the product of those numbers positioned at even locations where these numbers are also multiples of the integer three.
    """
    product = 1  
    for i, v in enumerate(lst):
        if i % 2 == 0 and v % 3 == 0:  
            product *= v  
    return product