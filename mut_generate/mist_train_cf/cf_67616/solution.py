"""
QUESTION:
Create a function `extract_phone_numbers` that uses regular expressions to extract phone numbers from a given string, including international formats and extension formats. The function should return a list of extracted phone numbers. The phone numbers may be in the formats: +1-800-888-8888, (021)555-3119, or 021-555-3119 ext 1234.
"""

import re

def extract_phone_numbers(s):
    """
    Extract phone numbers from a given string.

    This function uses regular expressions to extract phone numbers in various formats, 
    including international formats and extension formats.

    Parameters:
    s (str): The input string to extract phone numbers from.

    Returns:
    list: A list of extracted phone numbers.
    """
    
    # Regular expression pattern to match phone numbers
    pattern = re.compile(
        r'((\+\d{1,2}-)?'          # International format (e.g., +1-)
        r'\(?(\d{3})\)?'           # Area code (e.g., (021) or 021)
        r'[-.\s]?'                 # Separator (e.g., -, ., or whitespace)
        r'(\d{3})'                 # Local number (e.g., 555)
        r'[-.\s]?'                 # Separator (e.g., -, ., or whitespace)
        r'(\d{4})'                 # Local number (e.g., 3119)
        r'(\s?(ext|x)\s?\d{1,4})?'  # Extension (e.g., ext 1234)
        r')', re.IGNORECASE)
    
    # Find matches and return them
    return [match[0] for match in pattern.findall(s)]