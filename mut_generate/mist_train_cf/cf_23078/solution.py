"""
QUESTION:
Write a SQL query to calculate the average grade of each student from the 'Students' table, considering only grades above 90, and sort the results in descending order based on the average grade. The query should return the student's name and their corresponding average grade.
"""

def student_average_grade(students):
    averages = {}
    for student in students:
        grades = [grade for grade in student['grades'] if grade > 90]
        if grades:
            averages[student['name']] = sum(grades) / len(grades)
    return dict(sorted(averages.items(), key=lambda item: item[1], reverse=True))