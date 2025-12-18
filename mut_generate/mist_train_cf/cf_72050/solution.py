"""
QUESTION:
Find the largest key in the outermost dictionary. 

Create a function called `find_largest_key` that takes a nested dictionary as input and returns the largest key from the outermost dictionary. The keys can be of any comparable data type, such as numbers or strings. The function should compare keys based on their values, finding the highest value for numbers or the lexicographically last for strings.
"""

def find_largest_key(input_dict):
    """
    This function finds the largest key in the outermost dictionary.
    
    Args:
    input_dict (dict): A nested dictionary with keys of comparable data type.
    
    Returns:
    The largest key from the outermost dictionary.
    """
    return max(input_dict.keys(), key=lambda k: k)