"""
QUESTION:
Write a function named `parse_xml` that takes an XML filename as input. The XML file is expected to have a root element named "people" containing multiple "person" elements, each with "id", "name", "age", "occupation", and "city" sub-elements. The function should parse the XML file, handle potential parsing or data-related errors, check for duplicate IDs, and output the content in a structured way. The function should also be able to handle missing or incorrectly formatted values.
"""

import xml.etree.ElementTree as ET

def parse_xml(xmlfile):
    
    # Error handling for XML parsing
    try:
        tree = ET.parse(xmlfile)
    except ET.ParseError:
        print("Error parsing the XML file")
        return
    except FileNotFoundError:
        print("File not found")
        return

    root = tree.getroot()
    people = {}

    for person in root:

        # Handling missing or incorrectly formatted fields
        try:
            id = person.find('id').text
            name = person.find('name').text
            age = int(person.find('age').text)
            occupation = person.find('occupation').text
            city = person.find('city').text
        except AttributeError:
            print("Missing field for a person")
            continue

        # Duplicate IDs check
        if id in people:
            print(f"Duplicate ID found for {name}")
            continue
        else:
            people[id] = {'Name': name, 'Age': age, 'Occupation': occupation, 'City': city}

    # Outputting the people in a structured way
    for id, details in people.items():
        print(f'ID: {id}, Name: {details["Name"]}, Age: {details["Age"]}, Occupation: {details["Occupation"]}, City: {details["City"]}')