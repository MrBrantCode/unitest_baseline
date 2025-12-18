"""
QUESTION:
Create a function `log_grade_message` that takes an integer score as input and logs a message based on the corresponding grade. The grade and its associated score range are as follows: "A+" (90-100), "A" (85-89), "B" (70-84), "C" (50-69), "D" (30-49), and "F" (0-29). If the score falls outside these ranges or corresponds to an invalid grade, log an error message.
"""

def log_grade_message(score):
    """
    Logs a message based on the corresponding grade for the given score.

    Args:
        score (int): The score to determine the grade.

    Returns:
        str: The grade message.
    """
    if score < 0 or score > 100:
        return "Error: Score is out of range (0-100)."
    elif score >= 90:
        return "Congratulations! You got an A+!"
    elif score >= 85:
        return "Great job! You got an A!"
    elif score >= 70:
        return "Well done! You got a B."
    elif score >= 50:
        return "You passed with a C."
    elif score >= 30:
        return "You got a D. Study harder next time."
    else:
        return "You failed with an F. You need to improve."