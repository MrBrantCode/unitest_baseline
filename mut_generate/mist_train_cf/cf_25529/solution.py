"""
QUESTION:
Create a function `classify_grades_decision_tree(grade)` that takes an integer grade as input and returns the corresponding letter grade. The grade ranges are: A (90-100), B (80-89), C (70-79), and D (60-69). If the grade is outside of these ranges, return 'Error: Grade not in range'.
"""

def classify_grades_decision_tree(grade):
    if grade in range(90, 101): 
        return 'A'
    elif grade in range(80,90): 
        return 'B'
    elif grade in range(70,80): 
        return 'C'
    elif grade in range(60,70): 
        return 'D'
    else:
        return 'Error: Grade not in range'