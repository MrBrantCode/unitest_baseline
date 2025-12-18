"""
QUESTION:
Calculate the average score for each subject across all students. Implement a function `calculate_average_scores` that takes a list of dictionaries representing students' information and returns a dictionary containing the average score for each subject. Each dictionary in the input list represents a student and contains keys for the student's name and their scores in various subjects. The function should calculate the average score for each subject and return a dictionary where the keys are the subjects and the values are the average scores rounded to two decimal places. The input list will not be empty and will only contain valid student information.
"""

def calculate_average_scores(students: list) -> dict:
    subject_scores = {}
    num_students = len(students)

    for student in students:
        for subject, score in student.items():
            if subject != 'name':
                subject_scores[subject] = subject_scores.get(subject, 0) + score

    for subject, total_score in subject_scores.items():
        subject_scores[subject] = round(total_score / num_students, 2)

    return subject_scores