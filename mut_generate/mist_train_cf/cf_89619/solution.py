"""
QUESTION:
Create a function called `decode_base64` that takes a Base64 encoded string as input and returns its corresponding string representation. The function should not use the base64 library and should handle padding characters ('=') at the end of the Base64 string. The function should have a time complexity of O(n), where n is the length of the input Base64 string.
"""

def decode_base64(base64_string):
    # Step 1: Convert Base64 string to binary representation
    lookup_table = {
        'A': '000000', 'B': '000001', 'C': '000010', 'D': '000011', 'E': '000100', 'F': '000101', 'G': '000110', 'H': '000111',
        'I': '001000', 'J': '001001', 'K': '001010', 'L': '001011', 'M': '001100', 'N': '001101', 'O': '001110', 'P': '001111',
        'Q': '010000', 'R': '010001', 'S': '010010', 'T': '010011', 'U': '010100', 'V': '010101', 'W': '010110', 'X': '010111',
        'Y': '011000', 'Z': '011001', 'a': '011010', 'b': '011011', 'c': '011100', 'd': '011101', 'e': '011110', 'f': '011111',
        'g': '100000', 'h': '100001', 'i': '100010', 'j': '100011', 'k': '100100', 'l': '100101', 'm': '100110', 'n': '100111',
        'o': '101000', 'p': '101001', 'q': '101010', 'r': '101011', 's': '101100', 't': '101101', 'u': '101110', 'v': '101111',
        'w': '110000', 'x': '110001', 'y': '110010', 'z': '110011', '0': '110100', '1': '110101', '2': '110110', '3': '110111',
        '4': '111000', '5': '111001', '6': '111010', '7': '111011', '8': '111100', '9': '111101', '+': '111110', '/': '111111'
    }
    
    binary_string = ""
    for char in base64_string:
        if char in lookup_table:
            binary_string += lookup_table[char]
    
    # Step 2: Combine binary representations of each character
    if len(binary_string) % 8 != 0:
        # Add padding zeros if necessary
        binary_string += "0" * (8 - len(binary_string) % 8)
    
    # Step 3: Convert binary string to original string representation
    original_string = ""
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        decimal_value = int(byte, 2)
        if decimal_value != 0:
            original_string += chr(decimal_value)
    
    # Step 4: Return the original string representation
    return original_string