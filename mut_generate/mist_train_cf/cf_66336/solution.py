"""
QUESTION:
Given a text string and two words `first` and `second`, return a list of words that appear immediately after `second` in the text, where `second` directly follows `first`. The text contains 1-1000 characters, is composed of lowercase English letters separated by spaces, and `first` and `second` are 1-10 lowercase English letters each.
"""

def findOcurrences(text, first, second):
    words = text.split()
    return [words[i+2] for i in range(len(words)-2) if words[i]==first and words[i+1]==second]