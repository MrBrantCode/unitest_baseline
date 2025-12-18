"""
QUESTION:
Write a function `calculate_average_marks` that takes a dictionary `student_records` as input, where the keys are the names of the students and the values are dictionaries representing different subjects and their respective marks (ranging from 0 to 100) for each student. 

The function should calculate the average marks for each subject, the overall average marks for each student, the highest and lowest marks for each subject across all students, the highest and lowest marks for all subjects for each student, and the subject with the highest and lowest average marks across all students. The function should handle dictionaries with multiple subjects.
"""

def calculate_average_marks(student_records):
    subjects = student_records[next(iter(student_records))].keys()

    # Calculate average marks for each subject
    subject_averages = {}
    for subject in subjects:
        total_marks = 0
        num_students = 0
        highest_mark = 0
        lowest_mark = 100

        for student in student_records:
            if subject in student_records[student]:
                marks = student_records[student][subject]
                total_marks += marks
                num_students += 1
                highest_mark = max(highest_mark, marks)
                lowest_mark = min(lowest_mark, marks)

        subject_averages[subject] = total_marks / num_students

    # Calculate overall average marks for each student
    student_averages = {}
    for student in student_records:
        total_marks = sum(student_records[student].values())
        num_subjects = len(student_records[student])
        student_averages[student] = total_marks / num_subjects

    # Calculate overall highest and lowest marks for all subjects for each student
    student_highest_marks = {}
    student_lowest_marks = {}
    for student in student_records:
        student_highest_marks[student] = max(student_records[student].values())
        student_lowest_marks[student] = min(student_records[student].values())

    # Determine subject with highest and lowest average marks across all students
    highest_average_subject = max(subject_averages, key=subject_averages.get)
    lowest_average_subject = min(subject_averages, key=subject_averages.get)

    return {
        "subject_averages": subject_averages,
        "student_averages": student_averages,
        "student_highest_marks": student_highest_marks,
        "student_lowest_marks": student_lowest_marks,
        "highest_average_subject": highest_average_subject,
        "lowest_average_subject": lowest_average_subject,
    }