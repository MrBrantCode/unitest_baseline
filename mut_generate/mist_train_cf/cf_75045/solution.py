"""
QUESTION:
Write a function `convert` that takes a numeric score and grade thresholds (F, D, C, B, A) as input and returns the corresponding letter grade. The function should handle scores out of range (less than 0 or greater than 100) by returning an error message. The grade thresholds should be customizable, with default values of F=60, D=70, C=80, B=90, and A=100.
"""

def convert(score, F=60, D=70, C=80, B=90, A=100):
    """
    This function takes a numeric score and grade thresholds (F, D, C, B, A) as input 
    and returns the corresponding letter grade. It handles scores out of range (less 
    than 0 or greater than 100) by returning an error message.

    Parameters:
    score (int): The numeric score to be converted to a letter grade.
    F (int): The lower threshold for an F grade. Defaults to 60.
    D (int): The lower threshold for a D grade. Defaults to 70.
    C (int): The lower threshold for a C grade. Defaults to 80.
    B (int): The lower threshold for a B grade. Defaults to 90.
    A (int): The lower threshold for an A grade. Defaults to 100.

    Returns:
    str: The letter grade corresponding to the input score, or an error message if the score is out of range.
    """
    
    if score < 0 or score > 100:
        return 'Error: input out of range'
    elif score < F:
        return 'F'
    elif score < D:
        return 'D'
    elif score < C:
        return 'C'
    elif score < B:
        return 'B'
    else:
        return 'A'