"""
QUESTION:
Create a function `get_product(d)` that calculates the product of all distinct dictionary values in a given dictionary `d`. The dictionary values are characters and their corresponding numerical equivalents are determined by their positions in the alphabet (a=1, b=2, c=3, etc.). The function should return the product of these numerical equivalents, ignoring duplicates.
"""

def get_product(d):
    d_numeric = {k: ord(v) - 96 for k, v in d.items()}
    distinct_values = set(d_numeric.values())
    
    product = 1
    for value in distinct_values:
        product *= value

    return product