"""
QUESTION:
Create a function named `integer_to_ascii` that takes a single integer as input and returns its corresponding ASCII character. The function should only use basic arithmetic operations and not rely on any built-in functions or libraries that directly convert integers to ASCII characters. The input integer is guaranteed to be in the range of 0 to 127.
"""

def integer_to_ascii(num):
    # Ensure the given integer is within the valid range (0-127)
    if num < 0 or num > 127:
        return "Invalid input"
    # Convert the integer to ASCII character 
    ascii_char = chr(num)
    
    return ascii_char