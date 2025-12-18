"""
QUESTION:
Create a function named `product_of_odd_indexed_keys` that calculates the product of dictionary values at odd-indexed keys. The keys should be considered in lexicographical order. The function should take a dictionary as input and return the calculated product. The function should not modify the original dictionary.
"""

def product_of_odd_indexed_keys(dictionary):
    """
    Calculate the product of dictionary values at odd-indexed keys.

    Args:
        dictionary (dict): Input dictionary.

    Returns:
        int: The product of dictionary values at odd-indexed keys.
    """
    keys = sorted(dictionary.keys())
    product = 1

    for i in range(len(keys)):
        if i % 2 != 0:
            product *= dictionary[keys[i]]

    return product