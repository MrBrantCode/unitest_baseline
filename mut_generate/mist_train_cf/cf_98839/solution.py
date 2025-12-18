"""
QUESTION:
Create a function `extract_currency_symbol` that takes a JSON object containing a country's currency information with a base64 encoded symbol in the "symbol" key. The function should decode the symbol and return it if it consists only of letters from the English alphabet and is of length between 1 to 4 letters.
"""

import base64

def extract_currency_symbol(json_data):
    """
    Extracts and decodes the currency symbol from the given JSON data.

    Args:
        json_data (dict): A dictionary containing country's currency information.

    Returns:
        str: The decoded currency symbol if it consists only of letters from the English alphabet and is of length between 1 to 4 letters. Otherwise, returns None.
    """
    decoded_symbol = base64.b64decode(json_data["symbol"]).decode("utf-8")
    if decoded_symbol.isalpha() and 1 <= len(decoded_symbol) <= 4:
        return decoded_symbol
    else:
        return None