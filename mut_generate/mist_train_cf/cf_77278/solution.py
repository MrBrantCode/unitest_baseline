"""
QUESTION:
Extract the "products" value from a given JavaScript code. 

Write a function named `extract_products` that takes a string of JavaScript code as input, extracts the JSON object assigned to `window.searchResult`, and returns the value associated with the "products" key. Assume the input string contains the assignment of a JSON object to `window.searchResult` and the "products" key exists in the JSON object.
"""

import re
import json

def extract_products(script_text):
    """
    Extracts the 'products' value from a given JavaScript code.
    
    Args:
    script_text (str): A string of JavaScript code containing the assignment of a JSON object to window.searchResult.
    
    Returns:
    The value associated with the 'products' key in the JSON object.
    """
    
    # Find the JSON string within the JavaScript code
    json_str = re.search('window.searchResult = ({.*?});', script_text, re.DOTALL).group(1)
    
    # Convert the JSON string to a Python dictionary
    data = json.loads(json_str)
    
    # Return the 'products' value
    return data["products"]