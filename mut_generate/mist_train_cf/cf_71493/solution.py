"""
QUESTION:
Create a function named `grade_students` that takes an array of students' integer scores as input, ranging from 0 to 100 inclusive, and returns an array of corresponding letter grades with +/- distinctions (A+ to F). The function should include error handling to catch and return "Invalid score" for negative numbers and scores above 100.
"""

def grade_students(scores):
    grades = []
    for score in scores:
        if score < 0 or score > 100:
            grades.append("Invalid score")
        else:
            if score >= 90:
                grades.append('A+' if score > 97 else 'A' if score > 93 else 'A-')
            elif score >= 80:
                grades.append('B+' if score > 87 else 'B' if score > 83 else 'B-')
            elif score >= 70:
                grades.append('C+' if score > 77 else 'C' if score > 73 else 'C-')
            elif score >= 60:
                grades.append('D+' if score > 67 else 'D' if score > 63 else 'D-')
            else:
                grades.append('F')
    return grades