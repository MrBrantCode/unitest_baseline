"""
QUESTION:
Write a function named `find_highest_number` that takes an XML string containing a 'numbers' tag with multiple 'number' tags as its child, and returns the highest number found within these 'number' tags. Do not use built-in max or sort functions, or any sorting algorithms.
"""

import xml.etree.ElementTree as ET

def find_highest_number(xml_data):
    """
    This function takes an XML string containing a 'numbers' tag with multiple 'number' tags as its child, 
    and returns the highest number found within these 'number' tags.

    Args:
        xml_data (str): The XML string containing 'numbers' tag.

    Returns:
        int: The highest number found within the 'number' tags.
    """
    root = ET.fromstring(xml_data)
    highest = 0
    for number in root.iter('number'):
        num = int(number.text)
        if num > highest:
            highest = num
    return highest