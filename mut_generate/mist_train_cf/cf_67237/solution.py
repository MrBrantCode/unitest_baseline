"""
QUESTION:
Create a function named `tuple_product_dict` that takes a list of tuples as input. The function should return a dictionary where each tuple in the input list is a key and the corresponding value is the product of the integers in the tuple.
"""

def tuple_product_dict(tuples_list):
    """
    This function takes a list of tuples as input and returns a dictionary 
    where each tuple is a key and the corresponding value is the product of the integers in the tuple.

    Args:
    tuples_list (list): A list of tuples.

    Returns:
    dict: A dictionary where each tuple in the input list is a key and the corresponding value is the product of the integers in the tuple.
    """
    return {t: eval('*'.join(map(str, t))) for t in tuples_list}