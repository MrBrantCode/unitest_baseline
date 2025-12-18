"""
QUESTION:
Create a function named `HexProcessor` that categorizes characters from a given hexadecimal code into four categories: 'Alphabets', 'Numerical', 'Special Characters', and 'Whitespace'. The function should take a hexadecimal string as input and return a dictionary with the categorized characters. The categorization rules are based on ASCII values: 'Numerical' (48-57), 'Alphabets' (65-90 and 97-122), 'Whitespace' (32), and all other characters as 'Special Characters'.
"""

def HexProcessor(hex_code):
    """
    Categorize characters from a given hexadecimal code into four categories: 
    'Alphabets', 'Numerical', 'Special Characters', and 'Whitespace'.

    Args:
        hex_code (str): A hexadecimal string.

    Returns:
        dict: A dictionary with the categorized characters.
    """
    categories = {'Alphabets': [], 'Numerical': [], 'Special Characters': [], 'Whitespace': []}
    decoded = bytes.fromhex(hex_code).decode('utf-8')
    
    for char in decoded:
        ascii_val = ord(char)
        if 48 <= ascii_val <= 57:  
            categories['Numerical'].append(char)
        elif 65 <= ascii_val <= 90:  
            categories['Alphabets'].append(char)
        elif 97 <= ascii_val <= 122:  
            categories['Alphabets'].append(char)
        elif ascii_val == 32:  
            categories['Whitespace'].append(char)
        else:
            categories['Special Characters'].append(char)
    return categories