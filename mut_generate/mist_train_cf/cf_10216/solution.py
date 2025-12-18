"""
QUESTION:
Write a function called `find_terms` that takes the sum of a geometric progression, the common ratio, and the number of terms as input, and returns the terms of the geometric progression as a list. The function should use the formula for the sum of a geometric series to calculate the first term. 

The function should be able to handle any number of terms, but in this case, it will be used to find 4 terms. The sum of the geometric progression should be 120, the common ratio should be 2, and the number of terms should be 4.
"""

def find_terms(sum, ratio, num_terms):
    """
    This function calculates the terms of a geometric progression given its sum, common ratio, and number of terms.

    Args:
    sum (float): The sum of the geometric progression.
    ratio (float): The common ratio of the geometric progression.
    num_terms (int): The number of terms in the geometric progression.

    Returns:
    list: A list of terms in the geometric progression.
    """
    first_term = sum / ((ratio ** num_terms) - 1) * (ratio - 1)
    terms = [first_term * (ratio ** i) for i in range(num_terms)]
    return terms