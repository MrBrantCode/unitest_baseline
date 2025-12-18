"""
QUESTION:
Create a function `get_summary_report` that takes a dictionary of student names and their scores as input. The dictionary should have been validated to ensure all scores are within the range of 0 to 100. The function should return a dictionary containing the following information: the highest score, the lowest score, and the number of students who scored above the average. Assume the input dictionary is not empty and contains only integers as scores.
"""

def get_summary_report(scores):
    """
    This function generates a summary report from a dictionary of student scores.
    
    Args:
        scores (dict): A dictionary containing student names as keys and their scores as values.
        
    Returns:
        dict: A dictionary containing the highest score, the lowest score, and the number of students who scored above the average.
    """

    # Calculate the highest score
    highest_score = max(scores.values())

    # Calculate the lowest score
    lowest_score = min(scores.values())

    # Calculate the average score
    average_score = sum(scores.values()) / len(scores)

    # Count the number of students who scored above the average
    above_average = sum(score > average_score for score in scores.values())

    # Create the summary report
    report = {
        "Highest Score": highest_score,
        "Lowest Score": lowest_score,
        "Number of Students above Average": above_average
    }

    return report