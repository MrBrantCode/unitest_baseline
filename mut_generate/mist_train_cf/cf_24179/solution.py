"""
QUESTION:
Calculate the GPA from a list of test scores. Create a function called `calculate_gpa` that takes a list of tuples, where each tuple contains a course code and the corresponding score. The GPA is calculated by averaging the scores. Assume scores range from 0 to 100.
"""

def calculate_gpa(scores):
    """
    Calculate the GPA from a list of test scores.

    Args:
        scores (list): A list of tuples, where each tuple contains a course code and the corresponding score.

    Returns:
        float: The calculated GPA.
    """
    total_score = sum(score for _, score in scores)
    return total_score / len(scores)