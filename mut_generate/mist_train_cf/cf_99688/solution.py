"""
QUESTION:
Write a function named `decode_currency_symbol` that takes a dictionary containing a country's currency information in JSON format as input, where the currency symbol is encoded in base64 format and stored in the "symbol" key. The function should decode the base64 encoded symbol and return it if it consists of only letters from the English alphabet and is of length between 1 to 4 letters. If the symbol is invalid, the function should return an error message.
"""

def decode_currency_symbol(data):
    decoded_symbol = base64.b64decode(data["symbol"]).decode("utf-8")
    if decoded_symbol.isalpha() and 1 <= len(decoded_symbol) <= 4:
        return decoded_symbol
    else:
        return "Invalid currency symbol!"