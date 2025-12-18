"""
QUESTION:
Create a function `create_product_dict` that takes a list of tuples as input and returns a dictionary where each tuple is a key and the product of the tuple elements is the corresponding value. The tuples contain two integers each.
"""

def create_product_dict(tuples):
    """
    This function takes a list of tuples as input and returns a dictionary 
    where each tuple is a key and the product of the tuple elements is the corresponding value.

    Args:
        tuples (list): A list of tuples, each containing two integers.

    Returns:
        dict: A dictionary where each tuple is a key and the product of the tuple elements is the corresponding value.
    """
    return {t: t[0]*t[1] for t in tuples}