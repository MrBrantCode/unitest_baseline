"""
QUESTION:
Design a function named `clean_binary_data` that takes a binary string as input and returns a new binary string containing only printable characters (ASCII values between 32 and 126 inclusive) converted to uppercase, without any whitespace characters. The function should achieve this in a time complexity of O(n), where n is the length of the binary data.
"""

def clean_binary_data(binary_data):
    cleaned_data = b''
    
    for char in binary_data:
        if char >= 32 and char <= 126:
            if char >= 97 and char <= 122:
                char -= 32
            cleaned_data += bytes([char])
    
    return cleaned_data