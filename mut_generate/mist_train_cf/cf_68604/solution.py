"""
QUESTION:
Create a function called `hex_to_rev_bin` that takes a string input `hex_num` representing a hexadecimal number, converts it to binary, reverses the binary string, and returns the result. 

Restrictions:
- If `hex_num` is not a string, return "Error: Please enter a string".
- If `hex_num` is not a valid hexadecimal number, return "Error: Input is not a hexadecimal number".

Additionally, create a function called `is_palindrome` that checks if the reversed binary string is a palindrome using recursion. This function should take a string `bin_str` as input and return `True` if it is a palindrome and `False` otherwise.
"""

def hex_to_rev_bin(hex_num):
    if not isinstance(hex_num, str):
        return "Error: Please enter a string"
    elif not check_hex(hex_num):
        return "Error: Input is not a hexadecimal number"
    else:
        # Convert hexadecimal to binary
        bin_num = bin(int(hex_num, 16))[2:]
        # Reverse binary number
        rev_bin = bin_num[::-1]
        return rev_bin

def check_hex(hex_num):
    try:
        int(hex_num, 16)
        return True
    except ValueError:
        return False

def is_palindrome(bin_str):
    # Check if the string is a palindrome
    if len(bin_str) < 2:
        return True
    elif bin_str[0] != bin_str[-1]:
        return False
    else:
        return is_palindrome(bin_str[1:-1])