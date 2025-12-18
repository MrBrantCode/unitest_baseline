"""
QUESTION:
Write a function `find_terms(sum, ratio, terms)` that takes three arguments: the sum of terms, the common ratio, and the number of terms in a geometric progression. The function should return the list of terms in the geometric progression. The common ratio and the number of terms are known, but the first term is unknown and must be calculated. The sum of the terms is given by the formula `sum = a * (r^n - 1) / (r - 1)`, where `a` is the first term, `r` is the common ratio, and `n` is the number of terms.
"""

def find_terms(sum, ratio, terms):
    """
    This function calculates the list of terms in a geometric progression given the sum of terms, 
    the common ratio, and the number of terms.
    
    Args:
    sum (float): The sum of the terms in the geometric progression.
    ratio (float): The common ratio of the geometric progression.
    terms (int): The number of terms in the geometric progression.
    
    Returns:
    list: A list of terms in the geometric progression.
    """
    first_term = sum * (ratio - 1) / ((ratio**terms) - 1)
    progression = [first_term * (ratio**n) for n in range(terms)]
    return progression