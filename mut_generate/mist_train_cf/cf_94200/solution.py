"""
QUESTION:
Design a function `convert_grade(grade, scale)` that takes a numerical grade and a grading scale as input, and returns the corresponding letter grade. The function should:

- Accept numerical grades within the range of 0 to 100 (inclusive) and handle both integer and floating-point input grades.
- Round the input grade to the nearest whole number before conversion.
- Support multiple grading scales, each with its own range and corresponding letter grades, and allow the user to specify which grading scale to use.
- Handle negative numerical grades as a special case and assign a corresponding letter grade.
- Return an error message if the user inputs an invalid grading scale or an invalid numerical grade.
- Include error handling for unexpected inputs, such as non-numeric grades or invalid grading scale inputs.
"""

def convert_grade(grade, scale):
    # Check if grade is within range
    if not (0 <= grade <= 100):
        return "Invalid grade. Grade should be between 0 and 100 (inclusive)."
    
    # Round grade to nearest whole number
    grade = round(grade)
    
    # Define grading scales
    grading_scales = {
        "scale1": {"A": (90, 100), "B": (80, 89), "C": (70, 79), "D": (60, 69), "F": (0, 59)},
        "scale2": {"A+": (95, 100), "A": (90, 94), "A-": (85, 89), "B+": (80, 84), "B": (75, 79), "B-": (70, 74), "C+": (65, 69), "C": (60, 64), "C-": (55, 59), "D+": (50, 54), "D": (45, 49), "D-": (40, 44), "F": (0, 39)},
        # Add more grading scales as needed
    }
    
    # Check if scale is valid
    if scale not in grading_scales:
        return "Invalid grading scale. Available scales: " + ", ".join(grading_scales.keys())
    
    # Convert grade to letter grade based on scale
    for letter_grade, (min_grade, max_grade) in grading_scales[scale].items():
        if min_grade <= grade <= max_grade:
            return letter_grade
    
    # Handle negative grades
    if grade < 0:
        return "Negative grade. Corresponding letter grade: F"
    
    return "Error: Grade conversion failed."