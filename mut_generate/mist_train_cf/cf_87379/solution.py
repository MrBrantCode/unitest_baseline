"""
QUESTION:
Write a function `convert_to_float` that takes a string as input, converts it to a float, and handles potential errors. The function should return `None` for invalid inputs, including empty strings, strings with leading or trailing whitespace characters, strings with multiple decimal points, and strings with negative signs in unexpected positions. The function should have a time complexity of O(n), where n is the length of the input string.
"""

def convert_to_float(input_string):
    # Check for empty string
    if input_string.strip() == '':
        return None
    
    # Remove leading/trailing whitespace characters
    input_string = input_string.strip()
    
    # Check for multiple decimal points
    if input_string.count('.') > 1:
        return None
    
    # Check for negative sign in unexpected positions
    if input_string.startswith('-') or input_string.endswith('-'):
        return None
    if '--' in input_string or '-.' in input_string or '.-' in input_string:
        return None
    
    try:
        # Attempt to convert string to float
        result = float(input_string)
    except ValueError:
        # Handle ValueError if input_string is not a valid float
        return None
    
    return result