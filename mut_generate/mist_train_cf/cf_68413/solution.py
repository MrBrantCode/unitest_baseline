"""
QUESTION:
Create a function `calculate_grade(mark)` that takes an integer `mark` between 0 and 100 as input. The function should return a string representing the grade based on the following criteria: 
81-100: "Grade A"
61-80: "Grade B"
41-60: "Grade C"
21-40: "Grade D"
0-20: "Grade E"
"""

def calculate_grade(mark):
    if mark >= 81 and mark <= 100:
        return "Grade A"
    elif mark >= 61 and mark <= 80:
        return "Grade B"
    elif mark >= 41 and mark <= 60:
        return "Grade C"
    elif mark >= 21 and mark <= 40:
        return "Grade D"
    else:
        return "Grade E"