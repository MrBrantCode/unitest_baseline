"""
QUESTION:
Calculate the posterior probability P(D | TP) given the following information: 
- The disease prevalence rate P(D) is 0.05. 
- The probability of a positive test given disease P(TP | D) is 0.99. 
- The probability of a negative test given no disease P(TN | ~D) is 0.97.
Use Bayes' theorem to compute P(D | TP), the probability that an individual has the disease D given a positive test result.
"""

def calculate_posterior_probability(prevalence_rate, positive_test_given_disease, negative_test_given_no_disease):
    """
    Calculate the posterior probability P(D | TP) using Bayes' theorem.

    Args:
    prevalence_rate (float): The disease prevalence rate P(D).
    positive_test_given_disease (float): The probability of a positive test given disease P(TP | D).
    negative_test_given_no_disease (float): The probability of a negative test given no disease P(TN | ~D).

    Returns:
    float: The posterior probability P(D | TP).
    """

    # Calculate the probability of an individual not having the disease
    no_disease_probability = 1 - prevalence_rate
    
    # Calculate the false positive rate
    false_positive_rate = 1 - negative_test_given_no_disease
    
    # Apply Bayes' theorem
    posterior_probability = (positive_test_given_disease * prevalence_rate) / (
        (positive_test_given_disease * prevalence_rate) + (false_positive_rate * no_disease_probability)
    )
    
    return posterior_probability

# Example usage:
prevalence_rate = 0.05
positive_test_given_disease = 0.99
negative_test_given_no_disease = 0.97

posterior_probability = calculate_posterior_probability(prevalence_rate, positive_test_given_disease, negative_test_given_no_disease)
print(f"The posterior probability P(D | TP) is approximately {posterior_probability:.4f}")