"""
QUESTION:
Create a function classify_logistic_regression that takes a list of floating point numbers as input and returns a list of corresponding labels. The labels are assigned based on the following rules: 
- values less than 0 are classified as "Negative Class"
- values between 0 and 0.5 are classified as "Close to Negative Class" if they are less than 0.3 and "Neutral Class" otherwise
- values between 0.5 and 1 are classified as "Neutral Class"
- values greater than 1 are classified as "Positive Class"
"""

def classify_logistic_regression(values):
    """
    Classify a list of floating point numbers based on logistic regression rules.

    Args:
    values (list): A list of floating point numbers.

    Returns:
    list: A list of corresponding labels.
    """
    return ["Negative Class" if value < 0 else 
            "Close to Negative Class" if 0 <= value < 0.3 else 
            "Neutral Class" if 0.3 <= value <= 1 else 
            "Positive Class" 
            for value in values]