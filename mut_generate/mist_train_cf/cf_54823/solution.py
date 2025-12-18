"""
QUESTION:
Create a function called `replace_words` that takes a string `s` and a list of word pairs `words` as input. The function should replace all occurrences of the first word in each pair with the second word in the pair within the string. The replacement should be case-sensitive.
"""

def replace_words(s, words):
    for word in words:
        s = s.replace(word[0], word[1])
    return s