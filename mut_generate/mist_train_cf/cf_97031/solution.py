"""
QUESTION:
Create a function named `calculate_grade` that takes a single numerical value `marks` between 0 and 100 as input and returns the corresponding grade based on the following grading system: 
- A+ for marks >= 95
- A for marks between 90 and 94
- B+ for marks between 85 and 89
- B for marks between 80 and 84
- C+ for marks between 75 and 79
- C for marks between 70 and 74
- D+ for marks between 65 and 69
- D for marks between 60 and 64
- F for marks < 60
The function should round decimal marks to the nearest integer and handle invalid inputs.
"""

def calculate_grade(marks):
    if not (0 <= marks <= 100):
        return "Invalid input"

    marks = round(marks)

    if marks >= 95:
        return 'A+'
    elif marks >= 90:
        return 'A'
    elif marks >= 85:
        return 'B+'
    elif marks >= 80:
        return 'B'
    elif marks >= 75:
        return 'C+'
    elif marks >= 70:
        return 'C'
    elif marks >= 65:
        return 'D+'
    elif marks >= 60:
        return 'D'
    else:
        return 'F'