"""
QUESTION:
Implement a function called `convert_seven_segment` that takes a list of 7-segment display codes as strings of 7 binary digits and returns a list of tuples where each tuple contains the corresponding decimal and hexadecimal representations. The function should support the digits 0-9 and the punctuation characters period (.), comma (,), colon (:), and semi-colon (;). If an invalid 7-segment code is encountered, the function should print an error message and return None.
"""

conversion_dict = {
    '0110000': ('0', '0x30'),
    '0000110': ('1', '0x31'),
    '1011011': ('2', '0x32'),
    '1001111': ('3', '0x33'),
    '1100110': ('4', '0x34'),
    '1101101': ('5', '0x35'),
    '1111101': ('6', '0x36'),
    '0000111': ('7', '0x37'),
    '1111111': ('8', '0x38'),
    '1101111': ('9', '0x39'),
    '0000001': ('.', '0x2E'),
    '0010010': (',', '0x2C'),
    '1110101': (':', '0x3A'),
    '1010001': (';', '0x3B'),
}

def convert_seven_segment(seven_segment_codes):
    binary_and_hexadecimal = []
    for code in seven_segment_codes:
        if code in conversion_dict:
            binary_and_hexadecimal.append(conversion_dict[code])
        else:
            print(f"Invalid 7-segment code: {code}")
            return None
    return binary_and_hexadecimal