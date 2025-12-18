"""
QUESTION:
Write a Python function named `evaluate_hidden_markov_model` that assesses whether increasing the number of hidden states in a Hidden Markov Model (HMM) enhances the probability of the training data. The function should take the number of hidden states as a parameter and return a string describing the impact of the number of hidden states on the model's performance. Assume the number of hidden states is unknown and the model is used for a collection of observations.
"""

def evaluate_hidden_markov_model(num_hidden_states):
    """
    Evaluates the impact of the number of hidden states in a Hidden Markov Model (HMM) on the probability of the training data.

    Args:
        num_hidden_states (int): The number of hidden states in the HMM.

    Returns:
        str: A string describing the impact of the number of hidden states on the model's performance.
    """
    if num_hidden_states > 0:
        return f"Increasing the number of hidden states to {num_hidden_states} can enhance the probability of the training data, but may result in overfitting."
    else:
        return "Invalid number of hidden states. Please enter a positive integer."