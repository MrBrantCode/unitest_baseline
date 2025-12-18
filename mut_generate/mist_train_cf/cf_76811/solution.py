"""
QUESTION:
Write a function named `reverse_rearrange_string` that takes a string as input, divides it into three distinct parts of lengths 10, 2, and the rest, rearranges these parts in reverse order, and converts the resulting string to uppercase.
"""

def reverse_rearrange_string(input_str):
    """
    Divides the input string into three parts of lengths 10, 2, and the rest,
    rearranges these parts in reverse order, and converts the resulting string to uppercase.

    Args:
        input_str (str): The input string to be rearranged.

    Returns:
        str: The rearranged string in uppercase.
    """
    # Divide the string into 3 parts
    part1 = input_str[0:10]
    part2 = input_str[10:12]
    part3 = input_str[12:]

    # Reverse the order of the parts and concatenate them
    output_str = part3 + part2 + part1

    # Convert to uppercase
    output_str = output_str.upper()

    return output_str