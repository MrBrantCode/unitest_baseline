"""
QUESTION:
Create a recursive function `grade_ascent(score)` that takes an integer score between 0 and 100 as input and returns the corresponding letter grade. If the score is less than 60, return "D"; between 60 and 69 (inclusive), return "C"; between 70 and 79 (inclusive), return "B"; and between 80 and 100 (inclusive), return "A". If the score is less than 0 or greater than 100, return "Error: Score range must be 0-100". The function should use recursive calls instead of ternary operators.
"""

def grade_ascent(score):
    if score > 100 or score < 0:
        return "Error: Score range must be 0-100"
    elif score < 60:
        return "D"
    elif score < 70:
        return "C"
    elif score < 80:
        return "B"
    elif score <= 100:
        return "A"
    else:
        return grade_ascent(score - 1)