"""
QUESTION:
Write a function that maps specific scores to corresponding labels. The function should take an integer score as input and return a string label based on the following conditions: 
- score 80 maps to "Good"
- score 90 maps to "Excellent"
- score 60 maps to "Average"
- all other scores map to "Other"
"""

def map_score_to_label(score):
    """
    Maps specific scores to corresponding labels.

    Args:
        score (int): The input score.

    Returns:
        str: The corresponding label.
    """
    if score == 80:
        return "Good"
    elif score == 90:
        return "Excellent"
    elif score == 60:
        return "Average"
    else:
        return "Other"