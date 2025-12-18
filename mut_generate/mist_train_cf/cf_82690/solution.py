"""
QUESTION:
Implement a function `find_most_extended_term(lexicon, group_alphabets)` that takes a list of strings `lexicon` and a list of characters `group_alphabets` as input. The function should return the longest string in `lexicon` that can be formed using only the characters in `group_alphabets`. If no such string exists, return `None`.
"""

def find_most_extended_term(lexicon, group_alphabets):
    lexicon.sort(key=len, reverse=True)
    group_alphabets = set(group_alphabets)
    for word in lexicon:
        if set(word).issubset(group_alphabets):
            return word
    return None