"""
QUESTION:
Implement a function `validate_grade(grade_value: str) -> bool` that takes a string representation of a grade value as input and returns `True` if the grade value is a valid floating-point number within the range of 0.0 to 100.0, inclusive, and `False` otherwise. The input string should contain only numeric characters and at most one decimal point.
"""

import re

def validate_grade(grade_value: str) -> bool:
    # Check if the input is a valid floating-point number within the specified range
    if re.match(r'^\d{1,3}(\.\d+)?$', grade_value):
        value = float(grade_value)
        if 0.0 <= value <= 100.0:
            return True
    return False