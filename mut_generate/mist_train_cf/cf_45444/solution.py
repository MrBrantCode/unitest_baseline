"""
QUESTION:
Develop a function named `switch_char_positions` that takes a string as input and returns a new string where characters at even-indexed positions are swapped with characters at odd-indexed positions. The function should handle strings of any length.
"""

def switch_char_positions(input_str):
    """
    This function takes a string as input, swaps characters at even-indexed positions 
    with characters at odd-indexed positions, and returns the resulting string.

    Parameters:
    input_str (str): The input string.

    Returns:
    str: The string with characters at even-indexed positions swapped with characters at odd-indexed positions.
    """
    str_list = list(input_str)
    for i in range(0, len(str_list)-1, 2):
        str_list[i], str_list[i+1] = str_list[i+1], str_list[i]
    return "".join(str_list)