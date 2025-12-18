"""
QUESTION:
Write a function named `parse_student_record` that takes a JSON string as input, accesses the student's science grade, and calculates the weighted average grade. The function should return a tuple containing the science grade and the weighted average grade. The weights for each subject are math - 40%, english - 30%, science - 30%.
"""

import json

def parse_student_record(json_string):
    """
    Parse a JSON string representing a student record, access the student's science grade, 
    and calculate the weighted average grade.

    Args:
    json_string (str): A JSON string representing the student record.

    Returns:
    tuple: A tuple containing the science grade and the weighted average grade.
    """
    data = json.loads(json_string)
    science_grade = data['grades']['science']['grade']

    math_score = data['grades']['math']['score']
    english_score = data['grades']['english']['score']
    science_score = data['grades']['science']['score']

    weighted_average_grade = (math_score * 0.4 + english_score * 0.3 + science_score * 0.3)
    return science_grade, weighted_average_grade