"""
QUESTION:
Create a Python function `assign_typing_role` that takes an integer `typing_speed` as input and returns a string representing the corresponding typing role based on the following criteria:
- 20-29 WPM
- 30-39 WPM
- 40-49 WPM
- 50-59 WPM

If the typing speed is outside of these ranges, the function should return "Below 20 WPM or above 59 WPM".
"""

def assign_typing_role(typing_speed: int) -> str:
    if 20 <= typing_speed <= 29:
        return "20-29 WPM"
    elif 30 <= typing_speed <= 39:
        return "30-39 WPM"
    elif 40 <= typing_speed <= 49:
        return "40-49 WPM"
    elif 50 <= typing_speed <= 59:
        return "50-59 WPM"
    else:
        return "Below 20 WPM or above 59 WPM"