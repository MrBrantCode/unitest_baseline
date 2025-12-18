"""
QUESTION:
Write a function named `decode_currency_symbol` that takes a JSON object as input, extracts the base64 encoded currency symbol from the "symbol" key, decodes it, and returns the decoded symbol if it consists only of letters from the English alphabet and is of length between 1 to 4 letters.
"""

import base64

def decode_currency_symbol(json_data):
    """
    Decodes the base64 encoded currency symbol from the 'symbol' key in the given JSON data.
    Returns the decoded symbol if it consists only of letters from the English alphabet and is of length between 1 to 4 letters.
    
    Args:
        json_data (dict): A JSON object containing the base64 encoded currency symbol.
    
    Returns:
        str: The decoded currency symbol or None if the symbol is invalid.
    """
    decoded_symbol = base64.b64decode(json_data["symbol"]).decode("utf-8")
    if decoded_symbol.isalpha() and 1 <= len(decoded_symbol) <= 4:
        return decoded_symbol
    else:
        return None