"""
QUESTION:
Write a function `parse_student_record` that takes a JSON string representing a student record as input, and returns a dictionary containing the student's science grade and weighted average grade. The JSON string has the following structure:
{
  "name": "string",
  "age": integer,
  "grades": {
    "math": {
      "score": integer,
      "grade": "string"
    },
    "english": {
      "score": integer,
      "grade": "string"
    },
    "science": {
      "score": integer,
      "grade": "string"
    }
  }
}
The weighted average grade is calculated using the following weights: math - 40%, english - 30%, science - 30%.
"""

import json

def parse_student_record(json_string):
    """
    This function takes a JSON string representing a student record as input, 
    and returns a dictionary containing the student's science grade and weighted average grade.
    
    Args:
        json_string (str): A JSON string representing a student record.
    
    Returns:
        dict: A dictionary containing the student's science grade and weighted average grade.
    """
    # Parse the JSON string
    student_record = json.loads(json_string)

    # Access the student's science grade
    science_grade = student_record["grades"]["science"]["grade"]

    # Calculate the weighted average grade
    math_score = student_record["grades"]["math"]["score"]
    english_score = student_record["grades"]["english"]["score"]
    science_score = student_record["grades"]["science"]["score"]

    weighted_average = (math_score * 0.4) + (english_score * 0.3) + (science_score * 0.3)

    return {
        "science_grade": science_grade,
        "weighted_average": weighted_average
    }