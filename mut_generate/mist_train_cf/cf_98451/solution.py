"""
QUESTION:
Design a function called `group_students_by_subject` that takes a list of student dictionaries as input, where each dictionary contains a "favorite_subject" key with a value of either "Math", "Science", or "English". The function should return a dictionary where the keys are the favorite subjects and the values are lists of students who have chosen that subject.
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