"""
QUESTION:
Write a function `isPrefixOfWord(sentence, searchWord)` that checks if `searchWord` is a prefix of any word in `sentence`. Return the 1-indexed position of the word where `searchWord` is a prefix. If `searchWord` is a prefix of more than one word, return the position of the first word. If no such word exists, return -1. The function should be case-sensitive and consider only lowercase English letters. The input constraints are: `1 <= sentence.length <= 100`, `1 <= searchWord.length <= 10`, and `sentence` consists of lowercase English letters and spaces.
"""

def isPrefixOfWord(sentence, searchWord):
    words = sentence.split()
    for i in range(len(words)):
        if words[i].startswith(searchWord):
            return i + 1
    return -1