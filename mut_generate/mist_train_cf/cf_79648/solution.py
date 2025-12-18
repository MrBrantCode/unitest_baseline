"""
QUESTION:
Write a function `sum_ord_lower(s)` that computes the sum of ordinal values of lowercase consonants found exclusively on odd indices of an input string `s` in reverse order. The function should only consider the input string `s` as an argument and return the computed sum.
"""

def sum_ord_lower(s):
    """ 
    Computes the sum of ordinal values of lowercase consonants found exclusively on odd indices
    in an input string in reverse order.
    """
    # define the characters of interest
    vowels = set('aeiou')
    consonants = set('abcdefghijklmnopqrstuvwxyz') - vowels

    # pick characters at odd indexes in reverse order
    odd_index_chars = s[-1::-2] 

    # Compute the sum of ordinal values of the interesting characters
    return sum(ord(c) for c in odd_index_chars if c in consonants)