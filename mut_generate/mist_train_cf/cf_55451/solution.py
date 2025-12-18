"""
QUESTION:
Create a function named `median_of_products` that takes a 2D list of integers as input, calculates the product of each sublist, and returns the median value of these products. The input list contains at least one sublist and each sublist contains at least one integer.
"""

from statistics import median
from functools import reduce
import operator

def median_of_products(mat):
    # calculate the product of each sublist
    products = [reduce(operator.mul, sublist, 1) for sublist in mat]
    # return the median value of those products
    return median(products)