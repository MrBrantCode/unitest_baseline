"""
QUESTION:
Implement a `verify_address` function that uses regular expressions to validate a cryptocurrency wallet address. The function should distinguish between Bitcoin (BTC), Ethereum (ETH), and Litecoin (LTC) addresses based on their specific formats. The function should return whether the address is valid and, if so, the type of cryptocurrency it belongs to. 

Bitcoin addresses should start with 1 or 3 and be 26-35 alphanumeric characters. Ethereum addresses should start with '0x' followed by 40 hexadecimal characters. Litecoin addresses should start with L or M and be 33-34 alphanumeric characters.
"""

import re

def verify_address(address):
    """
    Uses regular expressions to validate a cryptocurrency wallet address.
    
    Args:
    address (str): The cryptocurrency wallet address to be validated.

    Returns:
    tuple: A boolean indicating whether the address is valid and the type of cryptocurrency it belongs to.
    """

    # Bitcoin addresses start with 1 or 3 and are 26-35 alphanumeric characters
    btc = re.match('^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', address)
    # Ethereum addresses start with '0x' followed by 40 hexadecimal characters
    eth = re.match('^0x[a-fA-F0-9]{40}$', address)
    # Litecoin addresses start with L or M and are 33-34 alphanumeric characters
    ltc = re.match('^[LM][a-km-zA-HJ-NP-Z1-9]{26,33}$', address)

    if btc:
        return (True, "Bitcoin")
    elif eth:
        return (True, "Ethereum")
    elif ltc:
        return (True, "Litecoin")
    else:
        return (False, None)