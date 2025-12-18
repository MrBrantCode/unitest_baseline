"""
QUESTION:
Write a function `calculate_product(lst)` that takes a list of integers as input. The function should return the product of all elements in the list, with the following modifications: 
- If the product is divisible by 3 and greater than 100, return the product multiplied by 4.
- If the product is divisible by 3 and less than or equal to 100, return the product multiplied by 5.
- If the product is not divisible by 3 and greater than 100, return the product divided by 4 and rounded down to the nearest integer.
- If the product is not divisible by 3 and less than or equal to 100, return the product divided by 5 and rounded down to the nearest integer.
"""

def calculate_product(lst):
    product = 1
    for num in lst:
        product *= num
        
    if product % 3 == 0 and product > 100:
        return product * 4
    elif product % 3 == 0 and product <= 100:
        return product * 5
    elif product % 3 != 0 and product > 100:
        return int(product / 4)
    else:
        return int(product / 5)