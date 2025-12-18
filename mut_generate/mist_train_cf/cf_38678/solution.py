"""
QUESTION:
Write a function `extractCopyrightInfo` that takes a string `htmlSnippet` as input. The string contains a `div` element with the class `col-lg-12` and the copyright information in the format "Copyright &copy; <NAME> <YEAR>". Extract the name and the year, and return them as a tuple `(name, year)`. The name and year should be separated by the year being the last sequence of exactly four digits in the string.
"""

import re

def extract_copyright_info(htmlSnippet):
    pattern = r'Copyright &copy; (.+?) (\d{4})'
    match = re.search(pattern, htmlSnippet)
    if match:
        name = match.group(1)
        year = match.group(2)
        return (name, year)
    else:
        return None