"""
QUESTION:
Write a function `find_lexeme_len_from_fact(lexeme_series, word_len_fact)` that takes a string `lexeme_series` and an integer `word_len_fact` as inputs, and returns the number of words in `lexeme_series` with a length equal to the factorial of `word_len_fact`. The function should split the input string into individual words and compare their lengths to the factorial of the given number.
"""

import math

def find_lexeme_len_from_fact(lexeme_series, word_len_fact):
    lexeme_list = lexeme_series.split()
    exact_len = math.factorial(word_len_fact)
    exact_len_lexemes = [lex for lex in lexeme_list if len(lex) == exact_len]
    return len(exact_len_lexemes)