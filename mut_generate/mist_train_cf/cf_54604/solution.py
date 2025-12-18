"""
QUESTION:
Given a Bayes net with the structure X <- Y -> Z, determine the accurate representation of the joint probability distribution P(X, Y, Z) using the conditional dependencies in the network.
"""

def bayes_net_probability(x_prob_given_y, y_prob, z_prob_given_y):
    return y_prob * x_prob_given_y * z_prob_given_y