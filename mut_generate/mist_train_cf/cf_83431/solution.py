"""
QUESTION:
Write a function `areSentencesSimilar(sentence1, sentence2)` that takes two sentences as input and returns `True` if they are similar, and `False` otherwise. The sentences are similar if it is possible to swap an arbitrary sentence (possibly empty) inside one of these sentences such that the two sentences become equal.

The input sentences are lists of words separated by a single space with no leading or trailing spaces. Words consist of only uppercase and lowercase English letters. The length of the sentences is between 1 and 100.
"""

def areSentencesSimilar(sentence1: str, sentence2: str) -> bool:
    s1, s2 = sentence1.split(' '), sentence2.split(' ')
    while s1 and s2 and s1[0] == s2[0]:
        s1.pop(0)
        s2.pop(0)
    while s1 and s2 and s1[-1] == s2[-1]:
        s1.pop()
        s2.pop()
    return not s1 or not s2