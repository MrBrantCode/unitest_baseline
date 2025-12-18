"""
QUESTION:
Create a function `extract_dates` that takes a list of strings as input and returns a list of strings representing dates in the format DD/MM/YYYY found within the input strings. The function should use regular expressions to identify the dates. The dates should be in the format of exactly two digits for the day, two digits for the month, and four digits for the year, separated by forward slashes.
"""

import re

def extract_dates(sentences):
    """
    This function takes a list of strings as input and returns a list of strings representing dates 
    in the format DD/MM/YYYY found within the input strings.

    Args:
        sentences (list): A list of strings that may contain dates.

    Returns:
        list: A list of strings representing dates in the format DD/MM/YYYY.
    """
    date_pattern = "\d{2}/\d{2}/\d{4}"
    dates = []
    for sentence in sentences:
        dates.extend(re.findall(date_pattern, sentence))
    return dates