"""
QUESTION:
Write a function `parse_xml_string` that takes a string representing an XML document containing a list of persons as input. The XML document should have a root element named "people" and each person should be represented by a "person" element with "name" and "age" child elements. The function should return a list of dictionaries, where each dictionary represents a person with keys "name" and "age". The function should only include persons with an age of 27 or older in the output list. If the XML string is malformed or contains invalid data types, the function should catch the corresponding exceptions, print an error message, and continue processing.
"""

import xml.etree.ElementTree as ET

def parse_xml_string(xml_string):
    """
    This function takes a string representing an XML document containing a list of persons as input.
    The XML document should have a root element named "people" and each person should be represented by a "person" element with "name" and "age" child elements.
    The function returns a list of dictionaries, where each dictionary represents a person with keys "name" and "age".
    The function only includes persons with an age of 27 or older in the output list.
    If the XML string is malformed or contains invalid data types, the function catches the corresponding exceptions, prints an error message, and continues processing.
    """

    person_list = []

    try:
        root = ET.fromstring(xml_string)
    except ET.ParseError as e:
        print(f"Parse Error: {str(e)}")
        return person_list

    for person in root.findall('person'):
        try:
            name = person.find('name').text
            age = int(person.find('age').text) 
            if age >= 27:
                person_list.append({"name": name, "age": age})
        except (AttributeError, ValueError) as e:
            print(f"Error processing person: {str(e)}")

    return person_list