"""
QUESTION:
Create a function named `parse_license` that takes a software license text as input. The function should extract the copyright year and permissions granted from the text. The copyright year is specified within parentheses after the "Copyright" keyword in the format of 4 digits separated by a hyphen, and the permissions are listed as bullet points starting with an asterisk and a space. The function should return the extracted copyright year and permissions.
"""

import re

def parse_license(license_text):
    """
    Extracts the copyright year and permissions from a software license text.

    Args:
        license_text (str): The software license text.

    Returns:
        tuple: A tuple containing the copyright year and a list of permissions.
    """

    copyright_year_match = re.search(r'Copyright \(c\) (\d{4} - \d{4})', license_text)
    permissions = re.findall(r'\* (.+)', license_text)
    
    copyright_year = copyright_year_match.group(1) if copyright_year_match else None

    return copyright_year, permissions