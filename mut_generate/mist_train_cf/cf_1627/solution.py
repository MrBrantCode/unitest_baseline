"""
QUESTION:
Calculate the checksum of a given string by converting it into ASCII values, summing them up, and then returning the remainder of the sum divided by 256. The function, named `calculate_checksum`, should take a string as input and return an integer checksum value. The input string can contain any printable ASCII characters and its maximum length is 100 characters. The function should handle edge cases such as empty strings or strings with only whitespace characters, returning 0 as the checksum value in those cases.
"""

def calculate_checksum(string):
    # Check if the string is empty or contains only whitespace characters
    if not string or string.isspace():
        return 0
    
    # Convert the string into ASCII values
    ascii_values = [ord(char) for char in string]
    
    # Calculate the sum of all the ASCII values
    checksum = sum(ascii_values)
    
    # Divide the sum by 256 to get the remainder
    checksum %= 256
    
    return checksum