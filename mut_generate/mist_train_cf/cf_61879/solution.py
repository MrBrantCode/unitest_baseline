"""
QUESTION:
Define a function `check_overfitting` that determines if a model is overfitting based on its cross-validation (CV) score and out-of-bag (OOB) score. The function should take two parameters: `cv_score` and `oob_score`, both representing F1 scores. The function should return a message indicating whether the model is overfitting or not, and if the degree of overfitting is acceptable based on a given tolerance. The tolerance should not be a fixed numerical threshold, but rather a general guideline that the CV score and OOB score should be as close to each other as possible.
"""

def check_overfitting(cv_score, oob_score):
    """
    Determine if a model is overfitting based on its cross-validation (CV) score and out-of-bag (OOB) score.

    Args:
        cv_score (float): The cross-validation F1 score.
        oob_score (float): The out-of-bag F1 score.

    Returns:
        str: A message indicating whether the model is overfitting or not, and if the degree of overfitting is acceptable.
    """

    # Calculate the difference between CV score and OOB score
    score_diff = abs(cv_score - oob_score)

    # If the difference is relatively small (less than 0.05), the model is not severely overfitting
    if score_diff < 0.05:
        return f"The model does not seem to be severely overfitting. The difference between CV score ({cv_score}) and OOB score ({oob_score}) is {score_diff}, which is relatively small."
    
    # If the difference is not small, the model is overfitting
    else:
        return f"The model seems to be overfitting. The difference between CV score ({cv_score}) and OOB score ({oob_score}) is {score_diff}, which is relatively large."