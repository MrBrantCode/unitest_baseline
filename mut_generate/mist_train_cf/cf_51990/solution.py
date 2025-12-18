"""
QUESTION:
Create a function named `subrout` that takes in a string `lexical_seq`, a character `alphabet_sym`, and an integer `count`, and returns `True` if `alphabet_sym` appears exactly `count` times in `lexical_seq`, and `False` otherwise.
"""

def subrout(lexical_seq, alphabet_sym, count):
    return lexical_seq.count(alphabet_sym) == count