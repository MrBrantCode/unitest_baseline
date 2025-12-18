"""
QUESTION:
Create a function to calculate and display the average, highest, and lowest marks for each subject given a dictionary of students with their respective marks in different subjects. The input dictionary should have student names as keys and another dictionary as values, where the inner dictionary has subject names as keys and marks as values.
"""

def calculate_student_marks(student_marks):
    """
    Calculate and display the average, highest, and lowest marks for each subject.

    Args:
    student_marks (dict): A dictionary with student names as keys and another dictionary as values.
                          The inner dictionary has subject names as keys and marks as values.

    Returns:
    tuple: A tuple containing three dictionaries - average_marks, highest_marks, and lowest_marks.
    """

    subject_marks = {}
    for student, marks in student_marks.items():
        for subject, mark in marks.items():
            if subject not in subject_marks:
                subject_marks[subject] = []
            subject_marks[subject].append(mark)

    average_marks = {subject: sum(marks) / len(marks) for subject, marks in subject_marks.items()}
    highest_marks = {subject: max(marks) for subject, marks in subject_marks.items()}
    lowest_marks = {subject: min(marks) for subject, marks in subject_marks.items()}

    return average_marks, highest_marks, lowest_marks

# or if the function should display the result instead of returning it:

def display_student_marks(student_marks):
    """
    Calculate and display the average, highest, and lowest marks for each subject.

    Args:
    student_marks (dict): A dictionary with student names as keys and another dictionary as values.
                          The inner dictionary has subject names as keys and marks as values.
    """

    subject_marks = {}
    for student, marks in student_marks.items():
        for subject, mark in marks.items():
            if subject not in subject_marks:
                subject_marks[subject] = []
            subject_marks[subject].append(mark)

    average_marks = {subject: sum(marks) / len(marks) for subject, marks in subject_marks.items()}
    highest_marks = {subject: max(marks) for subject, marks in subject_marks.items()}
    lowest_marks = {subject: min(marks) for subject, marks in subject_marks.items()}

    for subject in average_marks:
        print(f"Average marks for {subject}: {average_marks[subject]}")
        print(f"Highest marks for {subject}: {highest_marks[subject]}")
        print(f"Lowest marks for {subject}: {lowest_marks[subject]}")
        print()