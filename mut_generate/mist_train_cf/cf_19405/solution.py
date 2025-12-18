"""
QUESTION:
Write a function `parseMarkup` that takes a string representing a markup language as input and returns the sum of all numeric values found in the attributes of the markup. The markup language can contain nested elements, and attribute values can be integers or floating-point numbers. The function should handle malformed elements and attributes, ignore non-numeric attribute values, and handle scientific notation and decimal separators based on different locales. The function should also handle leading or trailing spaces in attribute values and attribute names.
"""

import re

def parseMarkup(markup: str) -> float:
    """
    This function takes a string representing a markup language as input and returns the sum of all numeric values found in the attributes of the markup.
    
    Args:
    markup (str): A string representing a markup language.
    
    Returns:
    float: The sum of all numeric values found in the attributes of the markup.
    """
    
    totalSum = 0
    
    # Regular expression pattern to match numeric values
    pattern = r"[\d\.]+(?:[eE][-+]?\d+)?"
    
    # Find all tags in the markup
    tags = re.findall(r"<[^>]*>", markup)
    
    for tag in tags:
        # Find all attribute-value pairs in the tag
        attribute_value_pairs = re.findall(r"(\w+)\s*=\s*['\"](.*?)['\"]", tag)
        
        for attribute, value in attribute_value_pairs:
            # Check if the value is a valid numeric value
            if re.fullmatch(pattern, value):
                # Parse the value to a float and add it to the totalSum
                totalSum += float(value)
    
    return totalSum