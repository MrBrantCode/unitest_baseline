"""
QUESTION:
Create a function named `base64_decode` that takes a Base64 encoded string as input and returns its corresponding string representation without using the base64 library. The function should handle padding characters and correctly decode the Base64 string to its original string representation.
"""

def base64_decode(base64_string):
    # Define the Base64 character set
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    # Initialize variables
    decoded_string = ""
    padding_count = 0
    padding_char = "="

    # Remove any padding characters from the end of the Base64 string
    if padding_char in base64_string:
        padding_count = base64_string.count(padding_char)
        base64_string = base64_string.rstrip(padding_char)

    # Convert the Base64 string to binary representation
    binary_string = ""
    for char in base64_string:
        char_value = base64_chars.index(char)
        binary_string += format(char_value, '06b')

    # Decode the binary string to the corresponding string representation
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        if len(byte) == 8:
            decoded_string += chr(int(byte, 2))

    # Add back any padding characters to the decoded string
    decoded_string = decoded_string[:-padding_count] if padding_count > 0 else decoded_string

    return decoded_string