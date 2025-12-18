"""
QUESTION:
Write a function called `calculate_grade_value` that takes a single character string representing a grade as input (e.g. 'A', 'B', 'C', 'D', 'F', or their lowercase equivalents) and returns the corresponding grade value. The function should handle both uppercase and lowercase letters and use fall-through behavior in the switch statement. Implement a logical error by including a default case that assigns an incorrect grade value.
"""

def calculate_grade_value(grade):
    grade = grade.upper()
    grade_value = {
        'A': 4.0,
        'B': 3.0,
        'C': 2.0,
        'D': 1.0,
        'F': 0.0
    }.get(grade, -1.0)  # default case with incorrect grade value
    return grade_value