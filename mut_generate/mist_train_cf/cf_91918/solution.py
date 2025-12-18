"""
QUESTION:
Write a function named `calculate_average_age` that takes a string of XML data as input, parses it to extract the age of each student, and returns the average age of all students. The XML data is in the format `<students><student><name>...</name><age>...</age></student>...</students>`. The function should have a time complexity of O(n), where n is the number of student records, and a space complexity of O(1), not using additional memory that grows with the input size.
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