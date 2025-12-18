"""
QUESTION:
Implement a function `calculate_grade` that takes the study time in hours as input and returns the new grade and the increase in grade, based on the correlation equation Grade = 50.25 + 10.2h.
"""

def calculate_grade(study_time):
    """
    This function calculates the new grade and the increase in grade based on the study time.

    Parameters:
    study_time (float): The study time in hours.

    Returns:
    tuple: A tuple containing the new grade and the increase in grade.
    """
    new_grade = 50.25 + 10.2 * study_time
    increase_in_grade = new_grade - 50.25
    return new_grade, increase_in_grade