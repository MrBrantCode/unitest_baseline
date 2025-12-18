"""
QUESTION:
Design a function `clean_binary_data` that takes binary data (a bytes object) as input, removes any non-printable characters, converts any lowercase letters to uppercase, and removes any whitespace characters from the data. The function should return the cleaned data as a string. The input binary data is encoded using UTF-8.
"""

def clean_binary_data(binary_data):
    """
    Cleans binary data by removing non-printable characters, 
    converting lowercase letters to uppercase, and removing whitespace characters.

    Args:
        binary_data (bytes): Binary data encoded using UTF-8.

    Returns:
        str: Cleaned data as a string.
    """
    # Convert binary data to string
    string_data = binary_data.decode('utf-8', errors='ignore')
    
    # Remove whitespace characters
    string_data = ''.join(string_data.split())

    # Filter out non-printable characters
    printable_chars = [char for char in string_data if char.isprintable()]

    # Convert lowercase letters to uppercase
    cleaned_data = ''.join(printable_chars).upper()

    return cleaned_data