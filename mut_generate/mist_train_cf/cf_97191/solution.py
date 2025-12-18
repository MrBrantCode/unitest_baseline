"""
QUESTION:
Design a function called `clean_binary_data` that takes binary data as input, removes any non-printable and whitespace characters, and converts any remaining lowercase letters to uppercase. The function should return the cleaned string data. The input binary data is encoded using UTF-8.
"""

def clean_binary_data(binary_data):
    # Convert binary data to string
    string_data = binary_data.decode('utf-8', errors='ignore')
    
    # Remove whitespace characters and filter out non-printable characters
    printable_chars = [char for char in string_data if char.isprintable() and not char.isspace()]

    # Convert lowercase letters to uppercase
    cleaned_data = ''.join(printable_chars).upper()

    return cleaned_data