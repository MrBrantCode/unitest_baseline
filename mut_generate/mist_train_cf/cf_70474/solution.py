"""
QUESTION:
Design a function `verify_word_set_frequency(expression1: str, expression2: str)` that takes two strings as input and returns a boolean value. The function should ascertain if the two input expressions have the same set of words with the same frequency, disregarding case sensitivity and word order.
"""

from collections import Counter

def verify_word_set_frequency(expression1: str, expression2: str) -> bool:
    """
    Ascertain if the two specified verbal expressions incorporate the precise same array of words with an equal incidence rate.
    As an illustration, the appearance of the word 'mango' recurring twice in the first verbal expression should coincide identically with twice occurrence in the second expression.
    """
    #Converting the sentences to lowercase to handle case sensitivity
    expression1 = expression1.lower()
    expression2 = expression2.lower()

    #Splitting the sentences into list of words
    words_in_expression1 = expression1.split()
    words_in_expression2 = expression2.split()

    #Counting the frequency of each word in the sentences : returning a dictionary
    count_exp1 = Counter(words_in_expression1)
    count_exp2 = Counter(words_in_expression2)

    #Checking if the word frequency dictionary of both sentences are equal
    return count_exp1 == count_exp2