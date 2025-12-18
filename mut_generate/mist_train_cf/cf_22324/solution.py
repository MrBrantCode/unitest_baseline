"""
QUESTION:
Create a function `calculate_grade(marks)` that takes a student's marks as a parameter and returns their corresponding grade based on the following grading system: 

- 95% and above: 'A+'
- 90-94%: 'A'
- 85-89%: 'B+'
- 80-84%: 'B'
- 75-79%: 'C+'
- 70-74%: 'C'
- 65-69%: 'D+'
- 60-64%: 'D'
- below 60%: 'F'

The function should also validate the input to ensure that the marks are within the range of 0 to 100, handle decimal marks by rounding them to the nearest integer, and have a time complexity of O(1) and space complexity of O(1).
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