"""
QUESTION:
Create a function `convert_grade` that takes a numerical grade between 1 and 100 as input and returns its corresponding letter grade equivalent. The grade ranges are: A (90-100), B (80-89), C (70-79), D (60-69), and F (below 60).
"""

def convert_grade(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'