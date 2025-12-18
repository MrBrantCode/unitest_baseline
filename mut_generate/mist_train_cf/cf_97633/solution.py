"""
QUESTION:
Write a function `decode_currency_symbol` that takes a JSON object containing a base64 encoded currency symbol in the "symbol" key. The function should decode the symbol and return it if it consists of only letters from the English alphabet and is of length between 1 to 4 letters.
"""

import base64

def decode_currency_symbol(json_data):
    decoded_symbol = base64.b64decode(json_data["symbol"]).decode("utf-8")
    if decoded_symbol.isalpha() and 1 <= len(decoded_symbol) <= 4:
        return decoded_symbol
    else:
        return None