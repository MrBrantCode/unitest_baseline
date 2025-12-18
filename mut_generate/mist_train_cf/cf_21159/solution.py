"""
QUESTION:
Write a function named `find_students` that takes a list of student records as input. Each record contains the student's name, score, and grade level. Return a list of student names who scored above 80 and have a grade level of 10 or above, sorted in descending order based on the student's score, and then by grade level in ascending order, and finally alphabetically by name. Ignore records with invalid grade levels (not a positive integer between 1 and 12) or scores.
"""

def find_students(records):
    # filter the records based on the criteria
    filtered_records = []
    for record in records:
        name, score, grade_level = record
        if isinstance(score, int) and score > 80 and isinstance(grade_level, int) and grade_level >= 10 and grade_level <= 12:
            filtered_records.append((name, score, grade_level))

    # sort the filtered records
    filtered_records.sort(key=lambda x: (-x[1], x[2], x[0]))

    # extract the names from the filtered records
    student_names = [record[0] for record in filtered_records]

    return student_names