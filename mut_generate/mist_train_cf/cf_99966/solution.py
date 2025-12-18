"""
QUESTION:
Create a function named `decode_currency_symbol` that takes a dictionary containing a base64 encoded currency symbol in the "symbol" key. The function should decode the symbol, check if it consists of only English letters and has a length between 1 to 4 letters, and return the decoded symbol if valid, otherwise return an error message.
"""

import base64

def decode_currency_symbol(data):
    decoded_symbol = base64.b64decode(data["symbol"]).decode("utf-8")
    if decoded_symbol.isalpha() and 1 <= len(decoded_symbol) <= 4:
        return decoded_symbol
    else:
        return "Invalid currency symbol!"