"""
QUESTION:
Write a function named char_to_binary that takes a string input from the user, converts each ASCII character to its corresponding binary representation in 8-bit format, and prints it along with the character. Restrict the function to only support ASCII characters, and handle non-ASCII characters by printing an error message. Additionally, implement error handling for invalid inputs such as empty strings. The function should not use any built-in functions or libraries that directly convert characters to ASCII values, including the ord() function.
"""

def char_to_binary(char):
    """
    This function converts a character to its corresponding binary representation in 8-bit format.
    
    Parameters:
    char (str): A single ASCII character
    
    Returns:
    str: The binary representation of the character in 8-bit format
    """
    # Create a string of 128 ASCII characters
    ascii_chars = [chr(i) for i in range(128)]
    
    # Check if the character is ASCII
    if char in ascii_chars:
        # Get the index of the character in the ascii_chars string
        ascii_value = ascii_chars.index(char)
        
        # Convert the ASCII value to binary and pad with leading zeros to make it 8-bit
        binary = bin(ascii_value)[2:]
        binary = '0' * (8 - len(binary)) + binary
        return binary
    else:
        print("Error: Non-ASCII characters are not supported.")
        return None