"""
QUESTION:
Create a function that takes an input string and returns its hex code representation. Additionally, verify that the generated hex code can be converted back to the original string. The function should handle dynamically inputted phrases or sentences and support ASCII characters. The function should output the hex code representation if the conversion is successful.
"""

import binascii

def entrance(text):
    # Convert text to hex
    return binascii.hexlify(text.encode()).decode('utf-8')