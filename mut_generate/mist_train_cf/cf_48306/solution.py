"""
QUESTION:
Create a Python function named `hex_to_decimal` that takes an array of hexadecimal strings as input, converts them to their corresponding decimal integers, and returns the decimal integers in an array. The function should be able to handle hexadecimal strings with both uppercase and lowercase alphabets, vary in length, and be efficient for large inputs. It should also include input validation to detect and report invalid hexadecimal strings.
"""

def hex_to_decimal(hex_array):
    decimal_array = []

    for hex_val in hex_array:
        try:
            # Using the built-in int function to convert hexadecimal to decimal
            decimal_val = int(hex_val, 16)
            decimal_array.append(decimal_val)
        except ValueError:
            # Detect invalid hexadecimal strings
            print(f"Invalid hexadecimal string detected: {hex_val}")
            continue
    return decimal_array