"""
QUESTION:
Create a function called `are_anagrams` that takes a list of strings `lexeme_collection` as input and returns `True` if all strings in the list are anagrams of each other, and `False` otherwise. The function should compare the strings regardless of their original order of characters.
"""

def are_anagrams(lexeme_collection):
    sorted_lexemes = [''.join(sorted(lexeme)) for lexeme in lexeme_collection]
    return all(lexeme == sorted_lexemes[0] for lexeme in sorted_lexemes)