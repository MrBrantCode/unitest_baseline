"""
QUESTION:
Extract Student Information from Nested XML Tags

Write a function named `extract_student_info` that takes a string containing a nested XML structure as input. The XML string may contain multiple 'student' tags at various levels within parent tags. Each 'student' tag has attributes: name, roll_no, course, and grade. The function should extract all 'student' tags and return their details, regardless of their depth within the XML structure.

Restrictions: The function should be able to handle any level of nested tags.
"""

import xml.etree.ElementTree as ET

def extract_student_info(xml_str):
    root = ET.fromstring(xml_str)
    student_info = []
    for student in root.iter('student'):
        student_details = {
            'name': student.get('name'),
            'roll_no': student.get('roll_no'),
            'course': student.get('course'),
            'grade': student.get('grade')
        }
        student_info.append(student_details)
    return student_info