"""
QUESTION:
Write a function called `find_highest_number` that takes an XML string containing a set of numbers enclosed within `<number>` tags as input, and returns the highest number without using built-in max or sorting functions. The input XML string is in the format `<numbers><number>num1</number><number>num2</number>...</numbers>`.
"""

import xml.etree.ElementTree as ET

def find_highest_number(xml_string):
    """
    This function takes an XML string containing a set of numbers enclosed within <number> tags as input, 
    and returns the highest number without using built-in max or sorting functions.

    Args:
        xml_string (str): An XML string containing a set of numbers enclosed within <number> tags.

    Returns:
        int: The highest number in the input XML string.
    """
    root = ET.fromstring(xml_string)
    highest = 0
    for number in root.iter('number'):
        num = int(number.text)
        if num > highest:
            highest = num
    return highest