"""
QUESTION:
Write a function named `convert_hex_to_ascii` that takes an array of hexadecimal strings as input, where each string represents one or more bytes. The function should return an array of ASCII strings, where each string is the equivalent of the corresponding input hexadecimal string. The input array is guaranteed to only contain valid hexadecimal strings with even lengths. The function should process each input string from left to right and return the result in the same order.
"""

def convert_hex_to_ascii(hex_array):
    ascii_array = []
    for hex_value in hex_array:
        ascii_value = ""
        for i in range(0, len(hex_value), 2):
            part = hex_value[i : i + 2]
            ch = chr(int(part, 16))
            ascii_value += ch
        ascii_array.append(ascii_value)
    return ascii_array