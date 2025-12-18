"""
QUESTION:
Write a function `parse_student_record` that takes a JSON string as input, accesses the student's science grade and calculates the weighted average grade based on the scores with weights: math - 40%, english - 30%, science - 30%. The function should return a tuple containing the student's science grade and the weighted average grade. The JSON string is expected to have the same structure as the given example.
"""

import json

def parse_student_record(json_string):
    """
    This function takes a JSON string as input, accesses the student's science grade and calculates the weighted average grade.
    
    Parameters:
    json_string (str): A JSON string representing the student record.
    
    Returns:
    tuple: A tuple containing the student's science grade and the weighted average grade.
    """
    
    # Parse the JSON string
    data = json.loads(json_string)
    
    # Access the student's science grade
    science_grade = data['grades']['science']['grade']
    
    # Calculate the weighted average grade
    math_score = data['grades']['math']['score']
    english_score = data['grades']['english']['score']
    science_score = data['grades']['science']['score']
    
    weighted_average_grade = (math_score * 0.4 + english_score * 0.3 + science_score * 0.3)
    
    return science_grade, weighted_average_grade