"""
QUESTION:
Find the largest number in a list of numbers enclosed in XML tags without using built-in sorting functions. The function should be named `find_largest_number`. The input is an XML string where numbers are enclosed in 'number' tags. Return the largest number found in the XML data. 

For example, given the XML string:
<numbers>
  <number>9</number>
  <number>12</number>
  <number>4</number>
  <number>7</number>
  <number>2</number>
</numbers>
the function should return 12.
"""

import xml.etree.ElementTree as ET

def find_largest_number(xml_data):
    """
    Find the largest number in an XML string where numbers are enclosed in 'number' tags.
    
    Args:
    xml_data (str): The input XML string.
    
    Returns:
    int: The largest number found in the XML data.
    """
    root = ET.fromstring(xml_data)
    numbers = [int(n.text) for n in root.findall('number')]
    largest_number = numbers[0]
    for num in numbers[1:]:
        if num > largest_number:
            largest_number = num
    return largest_number