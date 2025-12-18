"""
QUESTION:
Construct a function named `calculate_final_grade` that takes two dictionaries, `scores` and `weights`, as input. The `scores` dictionary contains category names as keys and the corresponding scores obtained as values, and the `weights` dictionary contains category names as keys and their respective percentage weights as values. The function should calculate the weighted average of the scores and return the final grade as a float. The weights are percentages and should be divided by 100 for calculation purposes. Assume that the category names in the `scores` and `weights` dictionaries are the same and that the weights add up to 100.
"""

def calculate_final_grade(scores, weights):
    """
        Calculate final grade based on weighted scores.
        
        Parameters:
        scores (dict): A dictionary containing category and score obtained.
        weights (dict): A dictionary containing category and weight. 
        
        Returns:
        final_grade (float): Final grade for the student.
    """
    weighted_scores = [scores[category] * (weights[category]/100) for category in scores]
    final_grade = sum(weighted_scores)
    return final_grade