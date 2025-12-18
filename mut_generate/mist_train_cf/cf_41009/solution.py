"""
QUESTION:
Implement a function `encodeWallet` that encodes a given wallet ID and code into a hexadecimal string. The function takes two parameters: `wallet` and `code`, both of which are strings consisting of alphanumeric characters. It should return a hexadecimal string representing the encoded wallet and code by concatenating the string "open wallet" with the wallet ID and code, and then converting the concatenated string into its hexadecimal representation.
"""

def encodeWallet(wallet, code):
    concatenated_str = "open wallet " + wallet + code
    encoded_hex = concatenated_str.encode('utf-8').hex()
    return encoded_hex