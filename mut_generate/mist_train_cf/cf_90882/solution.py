"""
QUESTION:
Write a function named `convert_to_string` that takes a list of characters as input and returns a string. The function should handle cases where the input list is empty or contains only whitespace characters, remove any leading or trailing whitespace characters from the resulting string, replace any consecutive whitespace characters within the input list with a single whitespace character in the resulting string, and preserve the original order of the characters in the input list. The function should also handle cases where the input list contains characters that are not valid ASCII characters, not printable ASCII characters, or not letters or digits.
"""

def convert_to_string(characters):
    # Handle case where input list is empty or contains only whitespace characters
    if not characters or all(char.isspace() for char in characters):
        return ''
    
    # Convert the list of characters into a string
    result = ''.join(characters)
    
    # Remove leading and trailing whitespace characters
    result = result.strip()
    
    # Replace consecutive whitespace characters with a single whitespace character
    result = ' '.join(result.split())
    
    # Check for non-ASCII characters
    try:
        result.encode('ascii')
    except UnicodeEncodeError:
        return 'Invalid ASCII characters found'
    
    # Check for non-printable ASCII characters
    if not all(char.isprintable() for char in result):
        return 'Non-printable ASCII characters found'
    
    # Check for characters that are not letters or digits
    if not all(char.isalnum() for char in result):
        return 'Invalid characters found'
    
    return result