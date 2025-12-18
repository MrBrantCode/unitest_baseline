"""
QUESTION:
Design a function named `convert_grade` that takes two arguments: `grade` and `grading_scale`, where `grade` is a numerical value between 0 and 100 (inclusive) and `grading_scale` is a dictionary representing the grading scale to be used. The function should round the input `grade` to the nearest whole number and return the corresponding letter grade based on the specified grading scale. The function should support multiple grading scales and handle cases such as negative numerical grades, invalid grading scales, non-numeric grades, and nested grading scales.
"""

def convert_grade(grade, grading_scale):
    if not isinstance(grade, (int, float)):
        return "Error: Invalid grade input"
    if not isinstance(grading_scale, dict):
        return "Error: Invalid grading scale input"

    grade = round(grade)
    if grade < 0:
        return "F"

    for scale, letter_grades in grading_scale.items():
        if isinstance(letter_grades, dict):
            return convert_grade(grade, letter_grades)
        if not isinstance(letter_grades, list) or len(letter_grades) < 2:
            return "Error: Invalid grading scale"

        min_grade, max_grade = letter_grades[0], letter_grades[-1]
        if min_grade <= grade <= max_grade:
            index = int((grade - min_grade) / (max_grade - min_grade) * (len(letter_grades) - 1))
            return letter_grades[index]

    return "Error: Invalid grading scale"