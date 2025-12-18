"""
QUESTION:
Write a function `bayesian_inference(P_B_given_A, P_A, P_B)` that calculates the conditional probability of event A occurring, given event B has occurred, using Bayes' theorem. The function should take as input the conditional probability of event B happening given event A (`P_B_given_A`), the individual probability of event A (`P_A`), and the particular probability of event B (`P_B`).
"""

def bayesian_inference(P_B_given_A, P_A, P_B):
    P_A_given_B = (P_B_given_A * P_A) / P_B
    return P_A_given_B