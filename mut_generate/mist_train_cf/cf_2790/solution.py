"""
QUESTION:
Write a function `convert_score_to_grade` to convert a given score to a grade. The function should take an integer score as input and return the corresponding grade as a string. The grading system is as follows: 
- A+: score > 95
- A-: 90 <= score <= 95
- B+: 85 <= score <= 89
- B: 80 <= score <= 84
- C: 70 <= score <= 79
- D: 60 <= score <= 69
- E: 50 <= score <= 59
- F: 0 <= score <= 49
- Error: Invalid score. Score cannot be negative. (for score < 0)
- Error: Invalid score. Score cannot be greater than 100. (for score > 100)
"""

def convert_score_to_grade(score: int) -> str:
    """
    This function converts a given score to a grade based on the following grading system:
    - A+: score > 95
    - A-: 90 <= score <= 95
    - B+: 85 <= score <= 89
    - B: 80 <= score <= 84
    - C: 70 <= score <= 79
    - D: 60 <= score <= 69
    - E: 50 <= score <= 59
    - F: 0 <= score <= 49
    - Error: Invalid score. Score cannot be negative. (for score < 0)
    - Error: Invalid score. Score cannot be greater than 100. (for score > 100)
    
    Parameters:
    score (int): The score to be converted
    
    Returns:
    str: The corresponding grade as a string
    """
    
    if score < 0:
        return "Error: Invalid score. Score cannot be negative."
    elif score > 100:
        return "Error: Invalid score. Score cannot be greater than 100."
    elif score > 95:
        return "A+"
    elif score > 90:
        return "A-"
    elif score > 85:
        return "B+"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    elif score >= 50:
        return "E"
    else:
        return "F"