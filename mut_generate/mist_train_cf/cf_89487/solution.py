"""
QUESTION:
Write a function `find_students` that takes a list of student records, where each record is a tuple containing the student's name, score, and grade level. The function should return a list of student names who scored above 80 and have a grade level of 10 or above, with a bonus of 5 points added to their score if it is above 90. The list should be sorted in descending order based on the student's score, and then by grade level in ascending order, and finally alphabetically by name. If a student's record does not have a valid grade level or score, it should be ignored.
"""

def find_students(records):
    valid_records = []
    for record in records:
        name, score, grade_level = record
        if isinstance(name, str) and isinstance(score, int) and isinstance(grade_level, int):
            if 1 <= grade_level <= 12 and score >= 0:
                valid_records.append((name, score, grade_level))

    valid_records = [(name, score + 5 if score > 90 else score, grade_level) for name, score, grade_level in valid_records]

    valid_records = [record for record in valid_records if record[1] > 80 and record[2] >= 10]

    valid_records = sorted(valid_records, key=lambda x: (-x[1], x[2], x[0]))

    return [name for name, _, _ in valid_records]