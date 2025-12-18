"""
QUESTION:
Create a function called `parse_xml()` that takes an XML string as input and parses it to extract 'student' and 'course' information with their attributes. The function should handle potential XML parsing errors and properly handle special characters. Assume the XML string is in the format `<student name="..." roll_no="..."> <course name="..." grade="..." /> </student>`.
"""

import xml.etree.ElementTree as ET

def parse_xml(xml_string):
    try:
        root = ET.fromstring(xml_string)

        for student in root.findall('student'):
            name = student.get('name')
            roll_no = student.get('roll_no')
            print(f"Student Name: {name}, Roll no: {roll_no}")

            for course in student.findall('course'):
                course_name = course.get('name')
                grade = course.get('grade')
                print(f"Course: {course_name}, Grade: {grade}")

    except ET.ParseError:
        print("The XML string is not well-formed.")
        return