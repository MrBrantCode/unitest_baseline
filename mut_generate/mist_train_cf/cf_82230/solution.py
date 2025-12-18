"""
QUESTION:
Write a function `product_of_keys` that calculates the product of all unique dictionary keys converted to integers. The function should handle dictionaries with both string and non-string keys, as well as nested dictionaries. The input dictionary will contain a mix of key types and values, including strings, integers, and nested dictionaries.
"""

def product_of_keys(d):
    product = 1

    for key in d:
        if isinstance(key, str) and key.isdigit():
            product *= int(key)

        elif isinstance(key, int):
            product *= key

        if isinstance(d[key], dict):
            product *= product_of_keys(d[key])

    return product