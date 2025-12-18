"""
QUESTION:
Design a function named `convert_string` that takes a string `s` as input, converts all uppercase letters in the string to lowercase, and replaces any numbers present within the string with their corresponding words (for example, '1' becomes 'one'). The function should return the modified string. The function should not use any external libraries and should handle digits as strings, not integers.
"""

def convert_string(s: str) -> str:
    number_map = {
        '0': 'zero','1': 'one','2': 'two','3': 'three','4': 'four',
        '5': 'five','6': 'six','7': 'seven','8': 'eight','9': 'nine'
    }

    # converting uppercase letters to lowercase
    result = s.lower()
    
    # replacing numbers with their corresponding words
    result = ''.join([number_map[i] if i.isdigit() else i for i in result])

    return result