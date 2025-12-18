"""
QUESTION:
Write a function `extract_employee_ids` to extract employee IDs from a given XML string. The XML string contains employee data with 'id', 'name', and 'department' elements. The function should return a list of employee IDs as strings. Use the `xml.etree.ElementTree` module to parse the XML string.
"""

import xml.etree.ElementTree as ET

def extract_employee_ids(xml_string):
    """
    Extracts employee IDs from a given XML string.

    Args:
        xml_string (str): The input XML string containing employee data.

    Returns:
        list: A list of employee IDs as strings.
    """
    root = ET.fromstring(xml_string)
    ids = [employee.find('id').text for employee in root.findall('employee')]
    return ids