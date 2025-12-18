"""
QUESTION:
Construct a function named `convert_score_to_grade` that takes an integer score as input, representing a student's test score, and returns the corresponding grade. The grade is determined by the following criteria: A (90-100), B (80-89), C (70-79), D (60-69), E (50-59), and F (below 50). If the input score is less than 0 or greater than 100, the function should return an error message 'Invalid score'.
"""

def convert_score_to_grade(score):
    """
    This function takes a student's test score and returns the corresponding grade.
    
    Parameters:
    score (int): The student's test score.
    
    Returns:
    str: The grade corresponding to the score, or an error message if the score is invalid.
    """
    
    if score < 0 or score > 100:
        return 'Invalid score'
    elif score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    elif score >= 50:
        return 'E'
    else:
        return 'F'