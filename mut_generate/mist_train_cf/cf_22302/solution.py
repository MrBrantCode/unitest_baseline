"""
QUESTION:
Write a function named `extract_data` that takes a single argument `xml_file`, which is the path to an XML file. The function should parse the XML file and extract data points from elements with a specific name and attribute value. Implement error handling to catch any parsing or data extraction errors and return an empty list in case of an error.
"""

import xml.etree.ElementTree as ET

def extract_data(xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        data_points = []

        for element in root.iter('element_name'):  
            if 'attribute_name' in element.attrib and element.attrib['attribute_name'] == 'desired_value':
                data = {}
                data['data_point1'] = element.find('nested_element1').text
                data['data_point2'] = element.get('attribute_name')
                data_points.append(data)

        return data_points

    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
    except Exception as e:
        print(f"Error extracting data: {e}")

    return []