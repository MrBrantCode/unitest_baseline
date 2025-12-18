"""
QUESTION:
Write a Python function named `parse_xml` that takes an XML string as input. This function should parse the XML string, extract specific data points based on multiple conditions, and handle any parsing or data extraction errors that may occur. The function should return a list of data points. The XML string may be encoded in a non-standard encoding format, such as UTF-16LE. The data points to be extracted are the text content of `<sub_element>` elements that are nested within `<item>` elements with a `status` attribute set to "active". If a `<sub_element>` exists and has non-empty text content, its text content should be included in the list of data points.
"""

import xml.etree.ElementTree as ET

def parse_xml(xml_string):
    try:
        # Parse XML string
        root = ET.fromstring(xml_string)

        # Check if XML document is encoded in non-standard encoding format
        encoding = root.get("encoding")
        if encoding and encoding.lower() == "utf-16le":
            xml_string = xml_string.encode("utf-16le").decode("utf-16le")

        # Extract data points based on conditions
        data_points = []
        for item in root.findall(".//item"):
            if item.get("status") == "active":
                sub_element = item.find("sub_element")
                if sub_element is not None and sub_element.text:
                    data_points.append(sub_element.text)

        return data_points

    except (ET.ParseError, AttributeError) as e:
        print("Error parsing XML:", e)
        return []