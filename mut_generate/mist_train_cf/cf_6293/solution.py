"""
QUESTION:
Create a function `alphanumeric_frequency_table` that takes a string of up to 1000 characters as input, excluding any special characters or whitespaces, and ignoring the case of the characters. The function should return a dictionary containing the frequency table of alphanumeric characters in the string, sorted in descending order of frequency.
"""

from collections import Counter
import re

def alphanumeric_frequency_table(input_string):
    input_string = re.sub(r'[^a-zA-Z0-9]', '', input_string).lower()
    frequency_table = Counter(input_string)
    return dict(sorted(frequency_table.items(), key=lambda x: x[1], reverse=True))