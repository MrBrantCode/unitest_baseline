"""
QUESTION:
Calculate the posterior probability P(D | TP) of an individual being afflicted with a disease D given a positive diagnostic test result TP. Given: P(D) = 0.05 (prevalence of the disease), P(TP | D) = 0.99 (sensitivity of the diagnostic test), and P(TN | ¬D) = 0.97 (specificity of the diagnostic test). Assume P(¬D) = 1 - P(D) and P(TP | ¬D) = 1 - P(TN | ¬D). Implement the calculation using Bayes' theorem.
"""

def calculate_posterior_probability(prevalence, sensitivity, specificity):
    """
    Calculate the posterior probability P(D | TP) of an individual being 
    afflicted with a disease D given a positive diagnostic test result TP.

    Args:
    prevalence (float): The a priori probability of an individual being 
                        afflicted with the disease D.
    sensitivity (float): The true positive rate of the diagnostic test.
    specificity (float): The true negative rate of the diagnostic test.

    Returns:
    float: The posterior probability of an individual having the disease 
           given a positive test result.
    """
    # Calculate the probability of an individual not being afflicted with the disease
    probability_not_disease = 1 - prevalence
    
    # Calculate the probability of a false positive result
    false_positive_rate = 1 - specificity

    # Calculate the probability of a positive test result
    probability_positive_test = (sensitivity * prevalence) + (false_positive_rate * probability_not_disease)

    # Calculate the posterior probability using Bayes' theorem
    posterior_probability = (sensitivity * prevalence) / probability_positive_test

    return posterior_probability