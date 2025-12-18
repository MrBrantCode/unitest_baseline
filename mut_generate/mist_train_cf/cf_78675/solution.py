"""
QUESTION:
Create a function `numeric_to_alpha_grade(score)` that takes a numeric score between 1 and 100 and returns its corresponding alphabetic grade representation, including the possibility to add "+" and "-" modifiers to grades B through D. The function should return "Invalid score" if the input score is outside the valid range. Implement a more complex grading scale where A: 93-100, A-: 90-92, B+: 87-89, B: 83-86, B-: 80-82, C+: 77-79, C: 73-76, C-: 70-72, D+: 67-69, D: 63-66, D-: 60-62, and F: below 60.
"""

def numeric_to_alpha_grade(score):
    # check for range first
    if score < 0 or score > 100:
        return "Invalid score."

    if score >= 93: 
        return "A"
    elif score >= 90:
        return "A-"
    elif score >= 87:
        return "B+"
    elif score >= 83:
        return "B"
    elif score >= 80:
        return "B-"
    elif score >= 77:
        return "C+"
    elif score >= 73:
        return "C"
    elif score >= 70:
        return "C-"
    elif score >= 67:
        return "D+"
    elif score >= 63:
        return "D"
    elif score >= 60:
        return "D-"
    else:
        return "F"