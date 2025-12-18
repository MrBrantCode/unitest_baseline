"""
QUESTION:
Write a function `pumping_lemma_example()` that demonstrates a language which meets the pumping lemma for regular languages but does not meet the pumping lemma for context-free languages. The function should take an integer `n` as input and return a string in the language L = {0^n1^n2^n | n >= 0}.
"""

def pumping_lemma_example(n):
    """
    This function generates a string in the language L = {0^n1^n2^n | n >= 0}.
    
    Args:
        n (int): The number of repetitions for each character in the string.
    
    Returns:
        str: A string in the language L with n repetitions of each character.
    """
    return '0' * n + '1' * n + '2' * n