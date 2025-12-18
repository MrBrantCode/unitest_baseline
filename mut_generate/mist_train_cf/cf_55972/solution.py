"""
QUESTION:
Write a function called `isPrefixOfWord` that takes two parameters: `sentence` and `searchWord`. `sentence` is a string of lowercase English letters and spaces, and `searchWord` is a string of lowercase English letters. The function should return the 1-indexed position of the word in the `sentence` where `searchWord` is a prefix of that word. If `searchWord` is a prefix of more than one word, return the position of the first word (minimum index). If no such word exists, return -1. Assume 1 <= sentence.length <= 100 and 1 <= searchWord.length <= 10.
"""

def isPrefixOfWord(sentence: str, searchWord: str) -> int:
    words = sentence.split(' ')
    for i, word in enumerate(words):
        if word.startswith(searchWord):
            return i + 1
    return -1