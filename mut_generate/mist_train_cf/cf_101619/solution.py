"""
QUESTION:
Write a function named `extract_currency_symbol` that takes a dictionary `data` as input, where the dictionary contains a base64 encoded currency symbol in the key "symbol". The function should decode the symbol and return it if it consists of only English letters and has a length between 1 and 4. Otherwise, return "Invalid currency symbol!".
"""

import base64

def extract_currency_symbol(data):
    """
    Extracts and decodes a base64 encoded currency symbol from a dictionary.
    
    Args:
    data (dict): A dictionary containing a base64 encoded currency symbol in the key "symbol".
    
    Returns:
    str: The decoded currency symbol if it consists of only English letters and has a length between 1 and 4, otherwise "Invalid currency symbol!".
    """
    decoded_symbol = base64.b64decode(data["symbol"]).decode("utf-8")
    if decoded_symbol.isalpha() and 1 <= len(decoded_symbol) <= 4:
        return decoded_symbol
    else:
        return "Invalid currency symbol!"