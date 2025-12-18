"""
QUESTION:
Find a pair of distinct hexadecimal digits from a given series that, when multiplied, result in a predetermined product. The hexadecimal digits range from 0-9 and A-F, representing values 0-15. Given a series of hexadecimal numbers and a desired product, write a function `find_hex_pair` to identify the pair of digits that satisfy the multiplication condition.
"""

def find_hex_pair(hex_series, target_product):
    """
    Find a pair of distinct hexadecimal digits from a given series that, when multiplied, result in a predetermined product.

    Args:
    hex_series (list): A list of hexadecimal digits.
    target_product (int): The desired product.

    Returns:
    tuple: A pair of hexadecimal digits that satisfy the multiplication condition. If no pair is found, returns None.
    """

    # Convert hexadecimal digits to their corresponding integer values
    hex_values = [int(hex_digit, 16) for hex_digit in hex_series]

    # Create a set to store the hexadecimal values for efficient lookups
    hex_set = set(hex_values)

    # Iterate over the hexadecimal values
    for i in range(len(hex_values)):
        # Calculate the complement of the current value with respect to the target product
        complement = target_product / hex_values[i]

        # Check if the complement exists in the set of hexadecimal values and is not the same as the current value
        if complement in hex_set and complement != hex_values[i]:
            # Convert the current value and its complement back to hexadecimal and return them as a tuple
            return (hex(hex_values[i])[2:].upper(), hex(int(complement))[2:].upper())

    # If no pair is found, return None
    return None