"""
QUESTION:
Create a function `longest_word` that takes a sentence as input and returns the longest word that does not contain both the letters 'a' and 'b' and has a minimum length of 5 characters.
"""

def longest_word(sentence):
    words = sentence.split()
    longest = ""
    for word in words:
        if 'a' in word and 'b' in word:
            continue
        if len(word) >= 5 and len(word) > len(longest):
            longest = word
    return longest