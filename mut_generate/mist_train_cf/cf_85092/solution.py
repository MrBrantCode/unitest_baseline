"""
QUESTION:
Write a function named `calculate_icc` that calculates the Intraclass Correlation Coefficient (ICC) for a two-way random effects model, adapted for a scenario where the number of raters varies between subjects. The function should take a 2D list `ratings` as input where each sublist contains the ratings for a single subject, and return the calculated ICC value.
"""

import numpy as np

def calculate_icc(ratings):
    """
    Calculate the Intraclass Correlation Coefficient (ICC) for a two-way random effects model.

    Parameters:
    ratings (list of lists): A 2D list where each sublist contains the ratings for a single subject.

    Returns:
    float: The calculated ICC value.
    """
    
    # Calculate the mean of all ratings
    grand_mean = np.mean([rating for sublist in ratings for rating in sublist])
    
    # Calculate the mean of each subject's ratings
    subject_means = [np.mean(sublist) for sublist in ratings]
    
    # Calculate the variance of the subject means
    subject_variance = np.var(subject_means, ddof=1)
    
    # Calculate the variance of the ratings within each subject
    within_subject_variance = np.mean([np.var(sublist, ddof=1) for sublist in ratings])
    
    # Calculate the ICC
    icc = subject_variance / (subject_variance + within_subject_variance)
    
    return icc