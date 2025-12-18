"""
QUESTION:
Find the maximum potential score achievable given a set of numerical entities and their corresponding scores. Define a function `max_potential_score` that takes two lists of equal length as input: `numerical_set` and `score_attributions`, where the index of each numerical entity in `numerical_set` corresponds to its score attribution in `score_attributions`. The function should return the maximum score in `score_attributions`.
"""

def max_potential_score(numerical_set, score_attributions):
    """
    This function calculates the maximum potential score achievable given a set of numerical entities and their corresponding scores.
    
    Args:
    numerical_set (list): A list of numerical entities.
    score_attributions (list): A list of scores corresponding to the numerical entities.
    
    Returns:
    int: The maximum potential score achievable.
    """
    num_to_score = dict(zip(numerical_set, score_attributions))
    max_score = max(num_to_score.values())
    return max_score