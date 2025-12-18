"""
QUESTION:
Write a function called `parse_xml` that takes a string of XML data as input where the XML data is in the format of a list of 'person' elements, each containing 'name' and 'age' elements. The function should parse the XML data, filter out the 'person' elements where the 'age' is greater than 25, sort the remaining 'person' elements in ascending order based on their 'age', and return a list of the 'name' elements of the sorted 'person' elements. The function should not use any third-party libraries or frameworks.
"""

import xml.etree.ElementTree as ET

def parse_xml(xml_data):
    # Parse XML
    tree = ET.ElementTree(ET.fromstring(xml_data))
    root = tree.getroot()

    # Filter and sort nodes
    filtered_nodes = []
    for person in root.findall('person'):
        age = int(person.find('age').text)
        if age <= 25:
            filtered_nodes.append((age, person.find('name').text))

    sorted_nodes = sorted(filtered_nodes, key=lambda x: x[0])

    # Return names
    return [name for _, name in sorted_nodes]