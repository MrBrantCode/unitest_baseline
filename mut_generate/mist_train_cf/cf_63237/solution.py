"""
QUESTION:
Create a function named `score_grades` that takes two inputs: a list of grades and a dictionary mapping grades to scores. The function should return the sum of the scores corresponding to each grade. Assume that the input dictionary's keys are in ascending order and the grades in the input list are present as keys in the dictionary.
"""

def score_grades(grades, score_dict):
    """
    Calculate the sum of scores corresponding to each grade.

    Args:
        grades (list): A list of grades.
        score_dict (dict): A dictionary mapping grades to scores.

    Returns:
        int: The sum of the scores corresponding to each grade.
    """
    return sum(score_dict[grade] for grade in grades)