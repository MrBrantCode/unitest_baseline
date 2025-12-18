"""
QUESTION:
Construct a function `grade_score(score)` to assign a grade to a given score. The score is a number between 1 and 100. The grades and their corresponding score ranges are as follows: A+ (97-100), A (93-96), A- (90-92), B+ (87-89), B (83-86), B- (80-82), C+ (77-79), C (73-76), C- (70-72), D+ (67-69), D (63-66), D- (60-62), and F (below 60). If the input score is outside the range of 1 to 100, the function should return an error message.
"""

def grade_score(score):
    if score < 0 or score > 100:
        return "Invalid input! Score must be between 0 and 100."
    elif score >= 97:
        return "A+"
    elif score >= 93:
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