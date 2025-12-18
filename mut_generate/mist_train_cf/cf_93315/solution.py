"""
QUESTION:
Design a function called `clean_binary_data` that takes a bytes object as input, removes non-printable characters, and converts all letters to uppercase. The function should return the cleaned string.
"""

def clean_binary_data(binary_data):
    cleaned_data = ""
    for char in binary_data.decode():
        if char.isprintable():
            cleaned_data += char.upper()
    return cleaned_data