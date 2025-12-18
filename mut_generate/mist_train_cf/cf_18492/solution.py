"""
QUESTION:
Write a function called `sort_sublists_by_product` that takes a list of sublists as input, sorts the sublists in ascending order based on the product of their elements, and returns the sorted list. The product of a sublist's elements should be calculated by multiplying all elements together, regardless of the length of the sublist.
"""

def sort_sublists_by_product(sublists):
    """
    Sorts a list of sublists in ascending order based on the product of their elements.
    
    Args:
        sublists (list): A list of sublists containing numeric elements.
    
    Returns:
        list: The sorted list of sublists.
    """
    return sorted(sublists, key=lambda x: eval('*'.join(map(str, x))))