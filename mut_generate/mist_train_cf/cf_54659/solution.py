"""
QUESTION:
Calculate the probability of a specified number of duplicate questions between two exams. Each exam chooses 100 questions at random from a pool of 192 questions without duplicates. 

The function should take the total number of questions (N), the number of questions on each exam (n), and the number of duplicate questions (k) as inputs, and return the probability of k duplicates. Use the Hypergeometric Distribution formula P(X=k) = [C(K,k) * C(N-K, n-k)] / C(N,n), where K is the number of questions on the first test.
"""

import math

def probability_of_duplicates(N, n, k):
    """
    Calculate the probability of k duplicates between two exams using Hypergeometric Distribution.

    Args:
    N (int): The total number of questions.
    n (int): The number of questions on each exam.
    k (int): The number of duplicate questions.

    Returns:
    float: The probability of k duplicates.
    """

    # Calculate the probability using the Hypergeometric Distribution formula
    probability = (math.comb(n, k) * math.comb(N - n, n - k)) / math.comb(N, n)
    
    return probability