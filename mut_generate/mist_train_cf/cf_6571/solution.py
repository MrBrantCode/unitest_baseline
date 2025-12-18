"""
QUESTION:
Write a function `find_students` that takes a list of student records in the format `(name, score, grade_level)`. The function should return a list of student names who have a score above 80 and a grade level of 10 or above. The grade level should be a positive integer between 1 and 12. If a student's score is above 90, add 5 bonus points to their score. The output list should be sorted in descending order based on the student's score. If two students have the same score, they should be sorted based on their grade level in ascending order. If two students have the same score and grade level, they should be sorted alphabetically based on their names. If two students have the same score, grade level, and name, the function should be able to handle the tie based on the student's age, but this information is not provided in the input records, so this condition will not be met.
"""

def find_students(records):
    valid_records = []
    for record in records:
        name, score, grade_level = record
        if isinstance(name, str) and isinstance(score, int) and isinstance(grade_level, int):
            if 1 <= grade_level <= 12 and score >= 0:
                valid_records.append((name, score, grade_level))

    valid_records = [(name, score + 5 if score > 90 else score, grade_level) for name, score, grade_level in valid_records]

    valid_records = sorted(valid_records, key=lambda x: (-x[1], x[2], x[0]))

    return [name for name, _, _ in valid_records]