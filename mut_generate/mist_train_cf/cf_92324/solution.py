"""
QUESTION:
Write a function named `longest_word` that takes a list of words as input and returns the longest word that starts with a vowel and ends with a consonant. If no such word exists, the function should return None.
"""

def longest_word(word_list):
    longest = None
    
    for word in word_list:
        if word[0] in "aeiouAEIOU" and word[-1] not in "aeiouAEIOU":
            if longest is None or len(word) > len(longest):
                longest = word
    
    return longest