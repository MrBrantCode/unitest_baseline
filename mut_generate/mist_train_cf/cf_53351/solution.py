"""
QUESTION:
Write a function `match_date(date)` that takes a string representing a date as input and returns `True` if the date matches any of the following formats: dd/mm/yyyy, dd-mm-yyyy, yyyy/mm/dd, yyyy-mm-dd, d-m-yyyy, d/mm/yyyy. The function should use regular expressions to match the date formats.
"""

import re
def match_date(date):
    pattern1 = "\d{1,2}[-/]\d{1,2}[-/]\d{4}"  # pattern for dd/mm/yyyy or dd-mm-yyyy
    pattern2 = "\d{4}[-/]\d{1,2}[-/]\d{1,2}"  # pattern for yyyy/mm/dd or yyyy-mm-dd
    return bool(re.match(pattern1, date) or re.match(pattern2, date))  # return True if either of the patterns matches the date