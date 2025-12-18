"""
QUESTION:
Create a function 'count_letters(string_name)' that calculates the frequency distribution of each letter in 'string_name', ignoring case sensitivity and excluding non-alphabet characters. The function should return a dictionary where the keys are the unique letters in the string and the values are their corresponding frequencies.
"""

from collections import Counter
import re

def count_letters(string_name):
    # Remove non-alphabet characters and convert to lower case
    clean_string = re.sub(r'[^a-zA-Z]', '', string_name).lower()
    # Use collections.Counter to count the frequency of each letter
    return dict(Counter(clean_string))