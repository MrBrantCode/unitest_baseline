"""
QUESTION:
Write a function named product_of_first_n_odds() that calculates the product of the first n odd integers. The function should return the product as an integer. The input to the function will be an integer representing the number of odd integers to consider.
"""

def product_of_first_n_odds(n):
    product = 1
    i = 1
    count = 0
    while count < n:
        if i % 2 != 0:
            product *= i
            count += 1
        i += 1
    return product