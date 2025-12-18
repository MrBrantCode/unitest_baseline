"""
QUESTION:
Calculate the product of all odd numbers in a given array and return the result modulo 1000000007. Implement a function `solve(arr)` that takes an array of integers as input and outputs the product modulo 1000000007.
"""

def solve(arr):
    product = 1
    for num in arr:
        if num % 2 != 0:
            product = (product * num) % 1000000007
    return product