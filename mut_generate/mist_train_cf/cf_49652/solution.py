"""
QUESTION:
Develop a function named `str_to_bin` that takes an input string and returns its binary representation. The function should be able to handle diverse character sets, including emojis and special characters, and should validate the input for any unwanted characters, displaying an error message when needed.
"""

def str_to_bin(input_str):
    try:
        binary_string = ''.join(format(ord(c), '08b') for c in input_str)
        return binary_string
    except TypeError as e:
        return f"Error: Invalid character found in input string. {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"