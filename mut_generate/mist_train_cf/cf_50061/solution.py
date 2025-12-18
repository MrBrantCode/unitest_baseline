"""
QUESTION:
Create a function `reformat_dates(text)` that takes a string `text` as input, identifies date strings in the formats MM/DD/YYYY, DD-MM-YYYY, and MMM DD, YYYY (where MMM is the three-letter abbreviation of the month), and returns a list of these dates reformatted to YYYY-MM-DD.
"""

import re
from datetime import datetime

def reformat_dates(text):
    pattern = r'\b(?:\d{1,2}[-/]\d{1,2}[-/]\d{4}|\b[A-Z][a-z]{2} \d{1,2}, \d{4}\b)'
    matches = re.findall(pattern, text)
    reformatted_dates = []

    for match in matches:
        date = None
        if '/' in match:
            try:
                date = datetime.strptime(match, "%m/%d/%Y")
            except ValueError:
                pass
        elif '-' in match:
            try:
                date = datetime.strptime(match, "%d-%m-%Y")
            except ValueError:
                pass
        else:
            try:
                date = datetime.strptime(match, "%b %d, %Y")
            except ValueError:
                pass

        if date is not None:
            reformatted = date.strftime('%Y-%m-%d')
            reformatted_dates.append(reformatted)

    return reformatted_dates