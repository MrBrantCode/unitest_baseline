"""
QUESTION:
Write a function `get_science_grade` that takes a JSON string as input representing a student record with a nested "grades" object. The function should parse the JSON string and return the value of the student's science grade. The function must be able to handle the JSON string with the following structure:
{
  "name": string,
  "age": number,
  "grades": {
    "math": number,
    "english": number,
    "science": number
  }
}
"""

import json

def get_science_grade(json_string):
    """
    This function takes a JSON string as input representing a student record with a nested "grades" object.
    It parses the JSON string and returns the value of the student's science grade.
    
    Parameters:
    json_string (str): A JSON string representing the student record.
    
    Returns:
    int: The value of the student's science grade.
    """
    # Parse the JSON string into a dictionary
    student_record = json.loads(json_string)
    
    # Access the value of the student's science grade
    science_grade = student_record['grades']['science']
    
    # Return the science grade
    return science_grade