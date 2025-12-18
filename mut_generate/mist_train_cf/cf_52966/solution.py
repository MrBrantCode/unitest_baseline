"""
QUESTION:
Design a function named `process_string` that takes in a string as input. The function should return a dictionary where the keys are characters and the values are their corresponding frequencies. The function should ignore non-alphabetic characters, convert uppercase letters to lowercase, and sort characters with the same frequency in ascending order based on their ASCII values. The frequency of each character should be computed as a fraction of the total number of considered characters, rounded to the nearest 0.001 (3 decimal places).
"""

def process_string(input_string):
    """
    This function processes the input string to return a dictionary where the keys are characters and the values are their corresponding frequencies.
    It ignores non-alphabetic characters, converts uppercase letters to lowercase, and sorts characters with the same frequency in ascending order based on their ASCII values.
    The frequency of each character is computed as a fraction of the total number of considered characters, rounded to the nearest 0.001 (3 decimal places).

    Args:
        input_string (str): The input string to be processed.

    Returns:
        dict: A dictionary containing character frequencies.
    """

    # Filter out non-alphabetic characters and convert to lowercase
    processed_string = ''.join(c.lower() for c in input_string if c.isalpha())

    # Initialize a dictionary to store character frequencies
    char_frequency = {}

    # Count the frequency of each character
    for char in processed_string:
        char_frequency[char] = char_frequency.get(char, 0) + 1

    # Calculate the total number of considered characters
    total_chars = len(processed_string)

    # Compute the frequency as a fraction of the total characters and round to 3 decimal places
    for char in char_frequency:
        char_frequency[char] = round(char_frequency[char] / total_chars, 3)

    # Sort characters with the same frequency in ascending order based on their ASCII values
    sorted_chars = sorted(char_frequency.items(), key=lambda x: (-x[1], x[0]))

    # Return the sorted dictionary
    return dict(sorted_chars)