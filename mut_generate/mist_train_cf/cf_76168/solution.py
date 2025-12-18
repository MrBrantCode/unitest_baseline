"""
QUESTION:
Create a function named `verify_bitcoin_address` that uses regular expressions to verify the format of a Bitcoin wallet address. The function should take a string `address` as input and return a boolean indicating whether the address matches the basic structure of a Bitcoin address, which starts with "1" or "3" and is 26-35 alphanumeric characters long.
"""

import re

def verify_bitcoin_address(address):
    match = re.match('^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', address)
    return bool(match)