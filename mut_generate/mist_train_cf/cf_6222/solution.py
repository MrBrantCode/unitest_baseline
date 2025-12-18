"""
QUESTION:
Write a function `grade_score` that takes an integer `score` between 0 and 100 as input and returns the corresponding letter grade based on the following grading criteria:
- 98 or above: A++
- 93-97: A+
- 90-92: A
- 87-89: A-
- 84-86: B+
- 80-83: B
- 77-79: B-
- 74-76: C+
- 70-73: C
- 67-69: C-
- 64-66: D+
- 60-63: D
- below 60: F
"""

def grade_score(score):
    """
    Returns the corresponding letter grade based on the given score.

    Args:
    score (int): An integer score between 0 and 100.

    Returns:
    str: The corresponding letter grade.
    """

    if score >= 98:
        return "A++"
    elif score >= 93:
        return "A+"
    elif score >= 90:
        return "A"
    elif score >= 87:
        return "A-"
    elif score >= 84:
        return "B+"
    elif score >= 80:
        return "B"
    elif score >= 77:
        return "B-"
    elif score >= 74:
        return "C+"
    elif score >= 70:
        return "C"
    elif score >= 67:
        return "C-"
    elif score >= 64:
        return "D+"
    elif score >= 60:
        return "D"
    else:
        return "F"