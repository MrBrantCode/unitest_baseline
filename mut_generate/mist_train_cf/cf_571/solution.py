"""
QUESTION:
Write a SQL query for a function named `filter_students` that filters records from the `StudentTable`. The query should include students who have a GPA greater than 3.5, are enrolled in the 'Computer Science' program, and have completed at least 60 credit hours. It should exclude students who have taken more than 5 elective courses and are not enrolled in any co-curricular activities.
"""

def filter_students(students):
    filtered_students = []
    for student in students:
        if (student['GPA'] > 3.5 and 
            student['Program'] == 'Computer Science' and 
            student['CreditHours'] >= 60 and 
            student['ElectiveCourses'] <= 5 and 
            student['CoCurricularActivities'] is not None):
            filtered_students.append(student)
    return filtered_students