"""
QUESTION:
Construct a function `construct_dict` that takes a list of tuples of integers as input and returns a dictionary where each tuple is a key, and the corresponding value is a list containing the product and division of the tuple elements, rounded to 2 decimal places. If the division is not possible (i.e., the denominator is 0), store "None" instead for that value.
"""

def construct_dict(tuples):
    result = {}
    for tup in tuples:
        product = tup[0] * tup[1]
        division = round(tup[0] / tup[1], 2) if tup[1] != 0 else None
        result[tup] = [product, division]
    return result