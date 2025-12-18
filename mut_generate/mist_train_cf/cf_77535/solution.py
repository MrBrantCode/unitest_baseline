"""
QUESTION:
Translate the string representation of an XML content into a dictionary object using Python. The XML content is about student information and includes nested elements such as 'courses' and 'grades'. The 'courses' element contains pairs of 'course' and 'grade' elements that should be parsed into a list of dictionaries. The function name should be `parse_student_xml`. Implement the function using the `xml.etree.ElementTree` module.
"""

import xml.etree.ElementTree as ET

def parse_student_xml(xml_data):
    """
    Translate the string representation of an XML content into a dictionary object.
    
    Args:
        xml_data (str): The XML content as a string.
    
    Returns:
        dict: A dictionary representation of the XML content.
    """
    
    root = ET.fromstring(xml_data)
    student_dict = {}
    
    for child in root:
        if len(child):
            courses_list = []
            for course, grade in zip(child[::2], child[1::2]):
                courses_list.append({'course': course.text, 'grade': grade.text})
            student_dict['courses'] = courses_list
        else:
            student_dict[child.tag] = child.text
    
    return student_dict