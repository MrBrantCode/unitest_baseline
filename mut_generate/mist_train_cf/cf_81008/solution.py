"""
QUESTION:
Write a function `hex_to_oct(hex_val)` that takes a hexadecimal number `hex_val` as input, converts it to octal, and returns the octal value along with a boolean indicating whether the octal value is a palindrome. The function should handle any potential errors or exceptions during the conversion.
"""

def hex_to_oct(hex_val):
    try:
        int_val = int(hex_val, 16)
        oct_val = oct(int_val).replace('0o', '')

        # Check if the number is a palindrome
        if oct_val == oct_val[::-1]:
            return oct_val, True
        else:
            return oct_val, False

    except:
        print("Error occurred while converting {0}".format(hex_val))