"""
QUESTION:
Write a function named `parse_xml` that takes an XML string as input. The function should parse the XML string, extract the 'name' fields of all 'person' nodes where the 'age' field is less than or equal to 25, sort these names in ascending order based on the corresponding 'age' fields, and return a list of the sorted names. The input XML string may contain nested nodes and multiple occurrences of the 'name' and 'age' fields.
"""

import xml.etree.ElementTree as ET

def parse_xml(xml_data):
    """
    Parse an XML string, extract 'name' fields of 'person' nodes where 'age' is <= 25,
    sort these names based on corresponding 'age' fields, and return a list of sorted names.
    
    Args:
    xml_data (str): The input XML string.
    
    Returns:
    list: A list of names in ascending order based on age.
    """
    
    # Parse the XML data
    root = ET.fromstring(xml_data)
    
    # Create a list to store valid name-age pairs
    name_age_pairs = []
    
    # Iterate through each 'person' node
    for person in root.findall('.//person'):
        name = person.find('name').text
        age = int(person.find('age').text)
        
        # Exclude nodes with age greater than 25
        if age <= 25:
            name_age_pairs.append((name, age))
    
    # Sort the name-age pairs based on age in ascending order
    name_age_pairs.sort(key=lambda x: x[1])
    
    # Return the names in ascending order based on age
    return [name for name, _ in name_age_pairs]