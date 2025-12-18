"""
QUESTION:
Create a function named `convert_to_grade(score)` that takes an integer score between 1 and 100 as input and returns its corresponding linguistic grade characterization. The grades and their corresponding score ranges are as follows: 'A' for scores 90-100, 'B' for scores 80-89, 'C' for scores 70-79, 'D' for scores 60-69, and 'F' for scores below 60. If the input score is outside the range of 1-100, the function should return an error message.
"""

def convert_to_grade(score):
    if not 1 <= score <= 100:
        return "Error: Score out of range. Enter a score between 1 and 100."
    elif score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'