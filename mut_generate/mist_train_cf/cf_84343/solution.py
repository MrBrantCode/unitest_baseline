"""
QUESTION:
Write a function named `xml_parser` that takes an XML string as input and returns a list of tuples containing the name, age, and role of each person, as well as a dictionary with the average age for each role. The XML string is expected to be in the format of a list of people with name, age, and role attributes.
"""

import xml.etree.ElementTree as ET
from collections import defaultdict

def xml_parser(xml):
    root = ET.fromstring(xml)
    people = root.findall('person')
    
    age_per_role = defaultdict(list)

    result = []

    for person in people:
        name = person.find('name').text
        age = int(person.find('age').text)
        role = person.find('role').text
        result.append((name, age, role))
            
        # Add age to corresponding role
        age_per_role[role].append(age)
            
    # Calculating average age
    avg_age_per_role = { role: sum(ages)/len(ages) for role, ages in age_per_role.items()}
    
    return result, avg_age_per_role