"""
QUESTION:
Write a function `calculate_student_marks` that takes a dictionary `student_mark_dict` where the keys are student names and the values are dictionaries containing subject names as keys and lists of marks as values. The function should calculate and return the average marks for each subject across all students, the overall average mark for each student, the highest and lowest marks for each subject across all students, the highest and lowest marks for each subject for each student, and the overall highest and lowest marks for all subjects for each student.
"""

def calculate_student_marks(student_mark_dict):
    # Calculate the average marks for each subject
    subject_avg_marks = {}
    for student in student_mark_dict:
        for subject, marks in student_mark_dict[student].items():
            if subject not in subject_avg_marks:
                subject_avg_marks[subject] = []
            subject_avg_marks[subject].extend(marks)
    for subject, marks in subject_avg_marks.items():
        subject_avg_marks[subject] = sum(marks) / len(marks)

    # Calculate the overall average mark for each student
    student_overall_avg_marks = {}
    for student, subjects in student_mark_dict.items():
        total_marks = 0
        total_subjects = 0
        for marks in subjects.values():
            total_marks += sum(marks)
            total_subjects += len(marks)
        student_overall_avg_marks[student] = total_marks / total_subjects

    # Calculate the highest and lowest marks for each subject for all students
    subject_highest_marks = {}
    subject_lowest_marks = {}
    for student in student_mark_dict:
        for subject, marks in student_mark_dict[student].items():
            if subject not in subject_highest_marks:
                subject_highest_marks[subject] = max(marks)
                subject_lowest_marks[subject] = min(marks)
            else:
                subject_highest_marks[subject] = max(subject_highest_marks[subject], max(marks))
                subject_lowest_marks[subject] = min(subject_lowest_marks[subject], min(marks))

    # Calculate the highest and lowest marks for each subject for each student
    student_highest_marks = {}
    student_lowest_marks = {}
    for student, subjects in student_mark_dict.items():
        student_highest_marks[student] = {subject: max(marks) for subject, marks in subjects.items()}
        student_lowest_marks[student] = {subject: min(marks) for subject, marks in subjects.items()}

    # Calculate the overall highest and lowest marks for all subjects for each student
    student_overall_highest_marks = {}
    student_overall_lowest_marks = {}
    for student, subjects in student_mark_dict.items():
        student_overall_highest_marks[student] = max([max(marks) for marks in subjects.values()])
        student_overall_lowest_marks[student] = min([min(marks) for marks in subjects.values()])

    return {
        'subject_avg_marks': subject_avg_marks,
        'student_overall_avg_marks': student_overall_avg_marks,
        'subject_highest_marks': subject_highest_marks,
        'subject_lowest_marks': subject_lowest_marks,
        'student_highest_marks': student_highest_marks,
        'student_lowest_marks': student_lowest_marks,
        'student_overall_highest_marks': student_overall_highest_marks,
        'student_overall_lowest_marks': student_overall_lowest_marks,
    }