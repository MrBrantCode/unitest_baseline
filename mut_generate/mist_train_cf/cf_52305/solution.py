"""
QUESTION:
Design a function `extract_info` that takes a string `text` as input and returns a tuple containing the Social Security Number, exact time, date of birth, and previous residential address extracted from the text. The function should assume that the input string always follows the same format and that the Social Security Number, time, date, and address are in the formats 'XXX-XX-XXXX', 'XX:XX AM/PM', 'XX/XX/XXXX', and 'XX XXX XXX, XXXX', respectively.
"""

import re

def extract_info(text):
    # compile regex for SSN, time, date and address
    re_ssn = re.compile(r'\d{3}-\d{2}-\d{4}')
    re_time = re.compile(r'\d{1,2}:\d{2} (AM|PM)')
    re_date = re.compile(r'\d{2}/\d{2}/\d{4}')
    re_address = re.compile(r'\d+ \w+ (Road|St|Ave), \w+')

    # search text for SSN, time, date, and address
    ssn = re_ssn.search(text)
    time = re_time.search(text)
    date = re_date.search(text)
    address = re_address.search(text)

    # return SSN, time, date, and address
    return ssn.group(), time.group(), date.group(), address.group()