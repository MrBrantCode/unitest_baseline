"""
QUESTION:
Write a function `calculate_occupied_tracks_percentage` that takes a 32-bit hexadecimal string as input, calculates the percentage of occupied tracks represented by '1' in the binary representation, and returns the result rounded to two decimal places. Assume that the input is a valid 32-bit hexadecimal string where '0' stands for vacant and '1' stands for occupied tracks.
"""

def calculate_occupied_tracks_percentage(hexadecimal_string):
    """
    Calculate the percentage of occupied tracks represented by '1' in the binary representation of a 32-bit hexadecimal string.

    Args:
        hexadecimal_string (str): A 32-bit hexadecimal string.

    Returns:
        float: The percentage of occupied tracks rounded to two decimal places.
    """
    binary = bin(int(hexadecimal_string, 16))[2:].zfill(32)
    total_occupied_tracks = binary.count('1')
    total_tracks = len(binary)
    occupied_percentage = (total_occupied_tracks / total_tracks) * 100
    return round(occupied_percentage, 2)