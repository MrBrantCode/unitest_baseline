"""
QUESTION:
Create a class named HexadecimalClassifier that takes a hexadecimal string as input. The class should unpack the hexadecimal string into a UTF-8 encoded string and have a method named classify that returns a dictionary containing the counts of alphabetic letters, numerical digits, void spaces, and distinctive sign characters in the unpacked string.
"""

def classify_hex(hex_string):
    unpacked_string = bytes.fromhex(hex_string).decode('utf-8')

    alpha_count = sum(c.isalpha() for c in unpacked_string)
    digit_count = sum(c.isdigit() for c in unpacked_string)
    space_count = sum(c.isspace() for c in unpacked_string)
    sign_count = len(unpacked_string) - alpha_count - digit_count - space_count

    return {
        "Alphabets": alpha_count,
        "Digits": digit_count,
        "Spaces": space_count,
        "Sign Characters": sign_count
    }