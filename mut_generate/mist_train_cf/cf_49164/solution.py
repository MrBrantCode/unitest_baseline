"""
QUESTION:
Create a function called `max_prod_pair` that accepts an array of integers as input and returns a list containing the pair of numbers with the maximum product. The input array must contain at least two elements.
"""

def max_prod_pair(array):
    if len(array) < 2:
        return None
    max_product = array[0] * array[1]
    max_pair = (array[0], array[1])
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            product = array[i] * array[j]
            if product > max_product:
                max_product = product
                max_pair = (array[i], array[j])
    return list(max_pair)