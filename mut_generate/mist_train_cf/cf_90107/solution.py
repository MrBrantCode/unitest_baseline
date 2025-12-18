"""
QUESTION:
Create a function called `calculate_grade` that takes in a single float parameter `marks`, representing a student's marks, and returns a string representing the corresponding grade. The function should handle decimal marks by rounding them to the nearest integer and should validate the input to ensure that the marks are within the range of 0 to 100. The grading system is as follows: 
- Marks above or equal to 95% are given an 'A+' grade.
- Marks between 90% and 94% (inclusive) are given an 'A' grade.
- Marks between 85% and 89% (inclusive) are given a 'B+' grade.
- Marks between 80% and 84% (inclusive) are given a 'B' grade.
- Marks between 75% and 79% (inclusive) are given a 'C+' grade.
- Marks between 70% and 74% (inclusive) are given a 'C' grade.
- Marks between 65% and 69% (inclusive) are given a 'D+' grade.
- Marks between 60% and 64% (inclusive) are given a 'D' grade.
- Marks below 60% are given an 'F' grade.
The function should handle negative marks by considering them as 0.
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