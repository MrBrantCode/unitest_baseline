"""
QUESTION:
Implement the `filter_students` function to filter a list of student records based on a given filter condition. The function should take in a list of student records and a filter condition as parameters and return a list of student names that satisfy the condition.

The `students` parameter is a list of dictionaries, where each dictionary represents a student record with keys "name" (string), "age" (integer), "grade" (string), and "school" (string).

The `filter_condition` parameter is a string that represents the filter condition, which can be one of the following:
- "high_grade": Return the names of students who are in grades 11 or 12.
- "teenagers": Return the names of students who are between 13 and 19 years old.
- "specific_school: <school_name>": Return the names of students who attend a specific school.

The function should return a list of names that satisfy the filter condition.
"""

from typing import List, Dict, Union

def filter_students(students: List[Dict[str, Union[str, int]]], filter_condition: str) -> List[str]:
    filtered_students = []
    
    if filter_condition == "high_grade":
        filtered_students = [student["name"] for student in students if student["grade"] in ["11", "12"]]
    elif filter_condition == "teenagers":
        filtered_students = [student["name"] for student in students if 13 <= student["age"] <= 19]
    elif filter_condition.startswith("specific_school:"):
        school_name = filter_condition.split(":")[1].strip()
        filtered_students = [student["name"] for student in students if student["school"] == school_name]
    
    return filtered_students