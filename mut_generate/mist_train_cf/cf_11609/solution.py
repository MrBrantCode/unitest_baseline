"""
QUESTION:
Write a function `calculate_average_age(xml_data)` that calculates the average age of all the students in the given XML data. The XML data is a string containing multiple `student` elements, each with a `name` and an `age`. The function should parse the XML data, extract the age values, calculate the average age, and return the result.

The function should have a time complexity of O(n), where n is the number of student records in the XML data, and a space complexity of O(1), meaning that it should not use additional memory that grows with the input size. The function should not use any external libraries for XML parsing, but may use the `xml.etree.ElementTree` module from Python's standard library.
"""

import xml.etree.ElementTree as ET

def calculate_average_age(xml_data):
    root = ET.fromstring(xml_data)
    total_age = 0
    num_students = 0

    for student in root.findall('student'):
        age = int(student.find('age').text)
        total_age += age
        num_students += 1

    average_age = total_age / num_students
    return average_age