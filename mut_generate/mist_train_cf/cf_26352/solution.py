"""
QUESTION:
Write a function `averageMarks` that calculates the average marks of all students given a dictionary where keys are student names and values are lists of their marks. The function should take a dictionary as input and return the average mark.
"""

def averageMarks(student_mark_dict):
    total = 0
    total_marks = 0
    for key, value in student_mark_dict.items():
        total += sum(value)
        total_marks += len(value)
        
    return total/total_marks