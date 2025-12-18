"""
QUESTION:
Implement the following functions to calculate student and subject averages, find the highest scoring student for a given subject, and find the subject with the highest average score.

- `calculate_student_average(scores: dict) -> dict`: 
  - Input: A dictionary `scores` where the keys are the student names and the values are lists of scores for each subject.
  - Output: A dictionary where the keys are the student names and the values are the average scores across all subjects, rounded to one decimal place.

- `calculate_subject_average(scores: dict) -> dict`:
  - Input: A dictionary `scores` where the keys are the student names and the values are lists of scores for each subject.
  - Output: A dictionary where the keys are the subject names ("Math", "English", "Physics", "Chemistry", "Biology") and the values are the average scores across all students, rounded to one decimal place.

- `find_highest_scoring_student(scores: dict, subject: str) -> str`:
  - Input: A dictionary `scores` where the keys are the student names and the values are lists of scores for each subject, and a string `subject` representing the subject for which the highest scoring student needs to be determined.
  - Output: The name of the highest scoring student for the given subject (return any one of their names if there's a tie).

- `find_subject_with_highest_average(scores: dict) -> str`:
  - Input: A dictionary `scores` where the keys are the student names and the values are lists of scores for each subject.
  - Output: The name of the subject with the highest average score across all students (return any one of their names if there's a tie).
"""

def calculate_student_average(scores: dict) -> dict:
    student_average = {}
    for student, scores_list in scores.items():
        average = sum(scores_list) / len(scores_list)
        student_average[student] = round(average, 1)
    return student_average

def calculate_subject_average(scores: dict) -> dict:
    subject_average = {}
    for student, scores_list in scores.items():
        for subject, score in zip(["Math", "English", "Physics", "Chemistry", "Biology"], scores_list):
            if subject in subject_average:
                subject_average[subject] += score
            else:
                subject_average[subject] = score
    for subject, total_score in subject_average.items():
        subject_average[subject] = round(total_score / len(scores), 1)
    return subject_average

def find_highest_scoring_student(scores: dict, subject: str) -> str:
    subjects = ["Math", "English", "Physics", "Chemistry", "Biology"]
    highest_score = float('-inf')
    highest_scoring_student = ""
    subject_index = subjects.index(subject)
    for student, scores_list in scores.items():
        score = scores_list[subject_index]
        if score > highest_score:
            highest_score = score
            highest_scoring_student = student
    return highest_scoring_student

def find_subject_with_highest_average(scores: dict) -> str:
    subject_average = calculate_subject_average(scores)
    highest_average = float('-inf')
    highest_average_subject = ""
    for subject, average in subject_average.items():
        if average > highest_average:
            highest_average = average
            highest_average_subject = subject
    return highest_average_subject