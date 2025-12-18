"""
QUESTION:
Create a function called `calculate_grade` that takes a single numeric argument representing a student's marks. The function should return the corresponding grade based on the following criteria:

- Marks 95 and above: 'A+'
- Marks 90-94: 'A'
- Marks 85-89: 'B+'
- Marks 80-84: 'B'
- Marks 75-79: 'C+'
- Marks 70-74: 'C'
- Marks 65-69: 'D+'
- Marks 60-64: 'D'
- Marks below 60: 'F'

The function should also:
- Validate the input to be within the range 0-100 and consider marks outside this range as 0 or 100.
- Round decimal marks to the nearest integer.
- Handle negative marks as 0.
- Handle marks exactly on the boundaries between two grades by giving the higher grade.
"""

def calculate_grade(marks):
    # Validate the input
    if marks < 0:
        marks = 0
    elif marks > 100:
        marks = 100
    
    # Round the marks to the nearest integer
    marks = round(marks)
    
    # Calculate the grade
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