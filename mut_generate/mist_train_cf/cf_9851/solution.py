"""
QUESTION:
Design a function named `convert_grade` that takes a numerical grade and an optional grading scale as input. The function should only accept grades within the range of 0 to 100 (inclusive) and round the input grade to the nearest whole number before conversion. It should support multiple predefined grading scales and return the corresponding letter grade based on the selected scale. If no grading scale is specified, it should default to a 'default' scale. The function should handle both integer and floating-point input grades.
"""

def convert_grade(grade, scale='default'):
    # Check if grade is within the range of 0 to 100
    if grade < 0 or grade > 100:
        return 'Invalid grade'

    # Round grade to the nearest whole number
    grade = round(grade)

    # Define grading scales
    grading_scales = {
        'default': {'A': (90, 100), 'B': (80, 89), 'C': (70, 79), 'D': (60, 69), 'F': (0, 59)},
        'scale1': {'A': (80, 100), 'B': (70, 79), 'C': (60, 69), 'D': (50, 59), 'F': (0, 49)},
        'scale2': {'A': (95, 100), 'B': (85, 94), 'C': (70, 84), 'D': (60, 69), 'F': (0, 59)}
    }

    # Get grading scale based on the input
    if scale not in grading_scales:
        return 'Invalid grading scale'
    scale = grading_scales[scale]

    # Convert grade to letter grade based on the selected grading scale
    for letter_grade, grade_range in scale.items():
        if grade >= grade_range[0] and grade <= grade_range[1]:
            return letter_grade