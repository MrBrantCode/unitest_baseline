"""
QUESTION:
Write a function `reversePrefix` that takes in a string `word` consisting of lowercase English letters only and a character `ch`, and returns the modified string where the substring from the beginning of `word` up to and including the first occurrence of `ch` is reversed, and the rest of `word` remains unchanged. If `ch` is not present in `word`, return the original `word` as is.
"""

def reversePrefix(word: str, ch: str) -> str:
    if ch in word:
        index = word.find(ch)
        return ''.join(reversed(word[:index + 1])) + word[index + 1:]
    else:
        return word