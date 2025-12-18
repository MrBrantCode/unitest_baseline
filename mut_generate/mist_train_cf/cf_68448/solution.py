"""
QUESTION:
Write a function `binary_operations` that takes a binary string as input and returns a tuple containing the decimal equivalent of the binary number, the count of 1s in the binary string, and the reversed binary string.
"""

def binary_operations(binary_string):
    """
    This function takes a binary string as input and returns a tuple containing 
    the decimal equivalent of the binary number, the count of 1s in the binary string, 
    and the reversed binary string.

    Args:
    binary_string (str): A string of binary digits.

    Returns:
    tuple: A tuple containing the decimal equivalent, count of 1s, and reversed binary string.
    """
    
    # Convert binary to decimal
    decimal = int(binary_string, 2)
    # Count number of 1s in binary string
    count_of_1s = binary_string.count('1')
    # Reverse the binary string
    reversed_string = binary_string[::-1]
    
    return decimal, count_of_1s, reversed_string