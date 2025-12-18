"""
QUESTION:
Write a function named `find_highest_number` that takes an XML string as input, where the string contains multiple `<number>` tags enclosed within a `<numbers>` tag, and returns the highest number among them. The function should not use any built-in sorting functions or formulas and should only rely on logical reasoning to find the solution.
"""

import xml.etree.ElementTree as ET

def find_highest_number(xml_data):
    """
    This function finds the highest number among multiple <number> tags enclosed within a <numbers> tag in an XML string.

    Args:
    xml_data (str): The input XML string.

    Returns:
    int: The highest number found in the XML data.
    """
    root = ET.fromstring(xml_data)
    highest = 0
    for number in root.iter('number'):
        num = int(number.text)
        if num > highest:
            highest = num
    return highest