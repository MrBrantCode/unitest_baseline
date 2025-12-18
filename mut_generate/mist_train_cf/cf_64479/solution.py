"""
QUESTION:
Write a function `bayes_theorem_allergy` that takes in the probability of having an allergy `allergy_rate`, the probability of a positive test result given that a person has the allergy `test_accuracy_positive`, and the probability of a negative test result given that a person does not have the allergy `test_accuracy_negative`. The function should return the probability of a person having the allergy given a negative test result using Bayes' Theorem.
"""

def bayes_theorem_allergy(allergy_rate, test_accuracy_positive, test_accuracy_negative):
    """
    Calculate the probability of a person having the allergy given a negative test result using Bayes' Theorem.

    Parameters:
    allergy_rate (float): The probability of having an allergy
    test_accuracy_positive (float): The probability of a positive test result given that a person has the allergy
    test_accuracy_negative (float): The probability of a negative test result given that a person does not have the allergy

    Returns:
    float: The probability of a person having the allergy given a negative test result
    """
    # Calculate the probability of not having the allergy
    not_allergy_rate = 1 - allergy_rate
    
    # Calculate the false negative rate
    false_negative_rate = 1 - test_accuracy_positive
    
    # Calculate the probability of a negative test result
    negative_test_rate = test_accuracy_negative * not_allergy_rate + false_negative_rate * allergy_rate
    
    # Calculate the probability of a person having the allergy given a negative test result using Bayes' Theorem
    return (false_negative_rate * allergy_rate) / negative_test_rate