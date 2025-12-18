"""
QUESTION:
Extract file names from an HTML string. 

Given an HTML string containing image tags with file names, write a function `extract_file_names(html_string)` that extracts the file names from the string. The function should return a list of file names without extensions. The HTML string may contain multiple image tags with the same file name pattern (e.g., "files/1/filename.jpg"). 

Restriction: The file name is between "files/1/" and ".jpg" in the HTML string.
"""

import re

def extract_file_names(html_string):
    """
    Extract file names from an HTML string.
    
    Args:
    html_string (str): The HTML string containing image tags with file names.
    
    Returns:
    list: A list of file names without extensions.
    """
    # Regular expression to identify filenames
    regex = r'(files\/1\/(.*?).jpg)'
    
    # Search in the string with the regular expression
    matches = re.findall(regex, html_string)
    
    # Mapping to get the filenames
    filenames = [match[1] for match in matches]
    
    return filenames