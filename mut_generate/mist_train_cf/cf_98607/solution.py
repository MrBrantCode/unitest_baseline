"""
QUESTION:
Implement a function called `evaluate_credit_score` that takes an `individual` object as input and returns their credit score. The `individual` object has attributes `ethnicity`, `gender`, and `income`. The function should evaluate the credit score based on these attributes.
"""

def evaluate_credit_score(individual):
    """
    Evaluates an individual's credit score based on their demographic information
    """
    score = 0
    
    # Ethnicity
    if individual.ethnicity == "Asian":
        score += 50
    elif individual.ethnicity == "Black":
        score += 30
    elif individual.ethnicity == "Hispanic":
        score += 20
    elif individual.ethnicity == "White":
        score += 10
    
    # Gender
    if individual.gender == "Female":
        score += 20
    
    # Income
    if individual.income >= 100000:
        score += 50
    elif individual.income >= 50000:
        score += 30
    elif individual.income >= 25000:
        score += 20
    elif individual.income >= 15000:
        score += 10
    
    return score