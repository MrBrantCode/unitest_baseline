"""
QUESTION:
Write a function `rearrange_fruits` that takes a list of fruit names as input and returns a string where the names are in alphabetical order, excluding any fruits that contain the letter "a" (case-insensitive), and the final string is reversed. The input list will only contain fruit names as strings.
"""

def rearrange_fruits(fruits):
    """
    This function takes a list of fruit names, removes fruits containing the letter "a" (case-insensitive), 
    sorts the remaining fruits alphabetically, and returns the result as a reversed string.

    Args:
    fruits (list): A list of fruit names as strings.

    Returns:
    str: A reversed string of the sorted fruit names without any fruits containing the letter "a".
    """
    
    # remove fruits with "a" (case-insensitive)
    fruits = [fruit for fruit in fruits if "a" not in fruit.lower()]
    
    # sort fruits alphabetically
    fruits.sort()
    
    # reverse and join the final string
    return "".join(fruits)[::-1]