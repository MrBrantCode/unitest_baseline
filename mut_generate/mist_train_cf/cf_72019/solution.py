"""
QUESTION:
Create a function `parse_xml_string(xml_str)` that takes an XML string as input, parses each element embedded within the 'student' and 'course details' tags, and returns a data structure containing the granularity of both 'student' and 'course' attributes. The function should also calculate the average grade for each student across all their courses. 

The XML string has the following structure:
```
<student name="Jane" roll_no="456">
    <course_details course="Mathematics" grade="A" />
    <course_details course="Physics" grade="B" />
</student>
```
Each student can have multiple courses, and multiple students can be present in the XML string. The function should handle repeated 'student' tags with different or similar attributes, maintaining unique students and appending their corresponding courses. The function should be efficient and scalable.
"""

import xml.etree.ElementTree as ET

class Course:
    def __init__(self, name, grade):
        self.name = name
        self.grade_letter_to_number = {"A": 5, "B": 4, "C": 3, "D": 2, "E": 1, "F": 0}
        self.grade = self.grade_letter_to_number[grade]

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def calc_avg_grade(self):
        total = 0
        for course in self.courses:
            total += course.grade
        return total/len(self.courses) if self.courses else 0

def parse_xml_string(xml_str):
    root = ET.fromstring(xml_str)
    
    # A dictionary to hold students objects keyed by roll_no
    students = {}

    # Parse XML and create objects
    for student in root.iter('student'):
        roll_no = student.attrib['roll_no']
        
        # If student does not exist, create new Student
        if roll_no not in students:
            students[roll_no] = Student(student.attrib['name'], roll_no)
        
        # Get the student's courses
        for course in student.iter('course_details'):
            students[roll_no].add_course(Course(course.attrib['course'], course.attrib['grade']))
    
    result = []
    for student in students.values():
        result.append({
            'name': student.name,
            'roll_no': student.roll_no,
            'average_grade': student.calc_avg_grade(),
            'courses': [{'name': course.name, 'grade': course.grade} for course in student.courses]
        })
    return result