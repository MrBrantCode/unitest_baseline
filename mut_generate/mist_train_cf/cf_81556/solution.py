"""
QUESTION:
Write a function `sample_average_approximation` that performs Sample Average Approximation (SAA) for a given objective function over a probability distribution. The function should take as input the objective function and a set of pre-available training samples, and return the approximate expected value of the objective function.

The training samples are assumed to be independently drawn from the probability distribution of interest. The function should not require sampling from the distribution, but instead use the provided training samples to calculate the approximate expected value.
"""

def sample_average_approximation(objective_function, training_samples):
    """
    This function performs Sample Average Approximation (SAA) for a given objective function over a probability distribution.
    
    Parameters:
    objective_function (function): The function for which we want to approximate the expected value.
    training_samples (list): A set of pre-available training samples drawn from the probability distribution of interest.
    
    Returns:
    float: The approximate expected value of the objective function.
    """
    # Calculate the average value of the objective function over all training samples
    return sum(objective_function(sample) for sample in training_samples) / len(training_samples)