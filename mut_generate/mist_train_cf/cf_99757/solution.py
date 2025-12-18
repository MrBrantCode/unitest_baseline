"""
QUESTION:
Write a function `find_missing_letter_and_frequency(xml_string)` that takes an XML string as input where the string contains a sequence of letters enclosed within `<data>` and `<sequence>` tags. The function should find the missing letter in the sequence (assuming the letters are in alphabetical order) and calculate the frequency of each letter in the sequence. The function should return a dictionary with two keys: `missing_letter` and `frequency`. The `missing_letter` key should contain the missing letter (if any) in the sequence, and the `frequency` key should contain a dictionary with the frequency of each letter in the sequence.
"""

import xml.etree.ElementTree as ET
from collections import Counter

def find_missing_letter_and_frequency(xml_string):
    # Parse the XML string to extract the sequence of letters
    root = ET.fromstring(xml_string)
    sequence = root.find('sequence').text.strip()
    # Find the missing letter in the sequence
    for i in range(len(sequence)-1):
        if ord(sequence[i+1]) - ord(sequence[i]) != 1:
            missing_letter = chr(ord(sequence[i]) + 1)
            break
    else:
        missing_letter = None
    # Calculate the frequency of each letter in the sequence
    frequency = Counter(sequence)
    # Return the results as a dictionary
    return {'missing_letter': missing_letter, 'frequency': dict(frequency)}