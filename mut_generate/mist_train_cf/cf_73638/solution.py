"""
QUESTION:
Create a function named `product_upto_n` that takes an integer `n` as input and returns the product of all numbers from 1 to `n` modulo 10^9 + 7. The function must be able to handle large inputs up to n = 10^5 efficiently.
"""

def product_upto_n(n):
    mod = 10**9 + 7
    product = 1
    i = 1
    while i <= n:
        product = (product * i) % mod
        i += 1
    return product