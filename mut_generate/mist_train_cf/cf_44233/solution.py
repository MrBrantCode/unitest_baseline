"""
QUESTION:
Create a function `longest_term(terminologies, numerical_symbols)` that determines the longest term that can be constructed exclusively from the allocated set of numerical symbols. The `terminologies` string contains a space-separated list of mathematical terms, and the `numerical_symbols` string contains the allowed numerical symbols. The function should return the longest term that only consists of the allowed numerical symbols. The function should assume that the input terms do not contain mathematical expressions with operators.
"""

def longest_term(terminologies, numerical_symbols):
    # Convert the string of terms into a list of words/terms
    terms = terminologies.split()
    # Convert the string of numerical symbols into a set for more efficient lookup
    symbols = set(numerical_symbols)
    longest = ""

    for term in terms:
        if set(term).issubset(symbols):
            if len(term) > len(longest):
                longest = term
    return longest