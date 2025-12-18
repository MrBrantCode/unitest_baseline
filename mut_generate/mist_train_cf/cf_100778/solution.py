"""
QUESTION:
Design a function named `group_students_by_subject` to group a list of students by their favorite subject among Math, Science, and English. Each student is represented as a dictionary containing their information, including their favorite subject. The function should return a dictionary where the keys are the favorite subjects and the values are lists of students who have chosen that subject.
"""

def group_students_by_subject(students):
    projects = {"Math": [], "Science": [], "English": []}
    for student in students:
        favorite_subject = student["favorite_subject"]
        if favorite_subject in projects:
            projects[favorite_subject].append(student)
        else:
            projects[favorite_subject] = [student]
    return projects