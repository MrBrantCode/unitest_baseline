"""
QUESTION:
Develop a function named `binary_to_decimal` that takes an array of binary strings as input. The function should convert each binary string to its corresponding decimal value, reorder the decimal values in descending order, remove any duplicates, and handle exceptions for invalid binary strings. The function should return an array of unique decimal values in descending order. If an invalid binary string is encountered, the function should print a customized error message and return without any output.
"""

def binary_to_decimal(bin_arr):
    """
    This function takes an array of binary strings, converts them to decimal values, 
    removes duplicates, and returns the unique decimal values in descending order.

    Args:
        bin_arr (list): A list of binary strings.

    Returns:
        list: A list of unique decimal values in descending order.
    """
    try:
        dec_arr = [int(s, 2) for s in bin_arr] # Convert binary to decimal
    except ValueError: # catch invalid binary input
        print("Error: The array contains an invalid binary string.")
        return
    
    dec_arr = list(set(dec_arr)) # Remove duplicates
    dec_arr.sort(reverse=True) # Sort in descending order

    return dec_arr