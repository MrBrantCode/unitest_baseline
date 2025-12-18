"""
QUESTION:
Create a function named `alphanumeric_frequency_table` that takes a string of up to 1000 characters as input, and returns a dictionary with the frequency of each alphanumeric character (ignoring case, special characters, and whitespaces) sorted in descending order of frequency.
"""

from collections import Counter
import re

def alphanumeric_frequency_table(input_string):
    # Remove special characters and whitespaces
    input_string = re.sub(r'[^a-zA-Z0-9]', '', input_string)
    
    # Convert to lowercase
    input_string = input_string.lower()
    
    # Count the frequency of alphanumeric characters
    frequency_table = Counter(input_string)
    
    # Sort the frequency table in descending order
    frequency_table = dict(sorted(frequency_table.items(), key=lambda x: x[1], reverse=True))
    
    return frequency_table