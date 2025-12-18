"""
QUESTION:
Create a function named `parse_xml` that takes an XML string as input. The function should parse the XML string, handle non-standard encoding formats, extract data points based on the following conditions: 
- the presence of an `<item>` element with a `status` attribute set to "active" 
- the presence of a `<sub_element>` within the `<item>` element with non-empty text content.
The function should return a list of extracted data points. Implement error handling to catch any parsing or data extraction errors.
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