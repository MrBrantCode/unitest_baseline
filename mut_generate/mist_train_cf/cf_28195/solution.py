"""
QUESTION:
Create a function `encode_string_hex` that takes a string and a list of encodings as input and returns a dictionary. The dictionary should contain the hexadecimal representation of the encoded bytes for each encoding. If the encoding process fails for a specific encoding, the dictionary should contain the string "ERROR" for that encoding. The function should return the dictionary with the hexadecimal representation of the encoded bytes in the format 'XX XX XX', where 'XX' is a hexadecimal byte.
"""

from typing import List, Dict, Union

def encode_string_hex(string: str, encodings: List[str]) -> Dict[str, Union[str, bytes]]:
    encoded_dict = {}
    for encoding in encodings:
        try:
            bytes = string.encode(encoding)
            dump = ' '.join('%02X' % byte for byte in bytes)
            encoded_dict[encoding] = dump
        except Exception as e:
            encoded_dict[encoding] = "ERROR"
    return encoded_dict