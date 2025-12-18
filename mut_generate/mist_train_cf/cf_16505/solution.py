"""
QUESTION:
Write a function `replace_last_occurrence` that takes a string and a word as input, and returns the string with the last occurrence of the word replaced, maintaining the original capitalization. The replacement should be case-insensitive and should only occur if the word is not part of another word.
"""

def replace_last_occurrence(string, word):
    words = string.split()
    for i in range(len(words)-1, -1, -1):
        if words[i].lower() == word.lower():
            if i == len(words)-1 or not words[i+1].isalpha():
                words[i] = words[i].replace(word, word, 1 if words[i].istitle() else -1)
                break
    return ' '.join(words)