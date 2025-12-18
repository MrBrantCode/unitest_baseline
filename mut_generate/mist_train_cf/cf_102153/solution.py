"""
QUESTION:
Create a function `calculate_statistics` that takes a dictionary `marks` as input. The dictionary contains student names as keys and another dictionary of subject names and marks as values. Calculate and return the average, highest, and lowest marks for each subject. Assume that the marks for each subject are the same across all students and all marks are non-negative integers.
"""

def calculate_statistics(marks):
    average_marks = {}
    highest_marks = {}
    lowest_marks = {}

    subjects = list(next(iter(marks.values())).keys())

    for subject in subjects:
        total_marks = 0
        highest_mark = float('-inf')
        lowest_mark = float('inf')

        for student, subject_marks in marks.items():
            if subject_marks[subject] > highest_mark:
                highest_mark = subject_marks[subject]
            if subject_marks[subject] < lowest_mark:
                lowest_mark = subject_marks[subject]
            total_marks += subject_marks[subject]

        average_marks[subject] = total_marks / len(marks)
        highest_marks[subject] = highest_mark
        lowest_marks[subject] = lowest_mark

    return {
        "average": average_marks,
        "highest": highest_marks,
        "lowest": lowest_marks
    }