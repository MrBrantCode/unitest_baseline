"""
QUESTION:
Write a function named `xml_to_dict` that takes a string representation of an XML data structure as input and returns a dictionary containing the student's details, including name, age, technical skill-set as a list of skills, and city. If the input XML string has a parsing error, the function should return the string "Error: Wrong xml format". The input XML string will be in the format `<student><name>...</name><age>...</age><skills>...</skills><city>...</city></student>`.
"""

import xml.etree.ElementTree as ET

def xml_to_dict(xml_str):
    try:
        root = ET.fromstring(xml_str)
        student_dict = {}
        for child in root:
            if child.tag == 'skills':
                skills = [skill.text for skill in child.iter('skill')]
                student_dict[child.tag] = skills
            else:
                student_dict[child.tag] = child.text
        return student_dict
    except ET.ParseError:
        return "Error: Wrong xml format"