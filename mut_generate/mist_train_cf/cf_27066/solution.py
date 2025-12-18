"""
QUESTION:
Write a function `get_module_status(xml_data)` that takes XML data as input and returns the status of a module. The XML data contains a `<status>` tag with the module status. If the status is "selected pending", return "selected pending"; otherwise, return "other status". The XML data may contain additional information and may not always be in the exact format, but the `<status>` tag will always be present.
"""

import xml.etree.ElementTree as ET

def get_module_status(xml_data):
    root = ET.fromstring(xml_data)
    status = root.find('status').text
    if status == "selected pending":
        return "selected pending"
    else:
        return "other status"