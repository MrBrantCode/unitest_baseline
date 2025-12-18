"""
QUESTION:
Write a function named `check(sentence)` that takes a sentence as input and returns a string describing whether the sentence is composed only of words that are palindromes and whether each of these palindromes are anagrams of each other. The function should handle punctuation, capitalization, and spaces, and consider a sentence with a single unique word as not having anagrams.
"""

import string

def check(sentence):
    def normalize(word):
        return word.strip(string.punctuation).lower()

    def is_palindrome(word):
        return word == word[::-1]

    def is_anagram(word, words):
        sorted_char_list = sorted(word)
        for _word in words:
            if sorted_char_list != sorted(_word):
                return False
        return True

    words = sentence.split()
    words = [normalize(word) for word in words]

    for word in words:
        if not is_palindrome(word):
            return "The sentence is not composed of palindromes."

    if len(set(words)) < 2: 
        return "The sentence is composed of palindromes. However, the words are not anagrams of each other."
    
    first_word = words[0]
    remainder_words = words[1:]

    if is_anagram(first_word, remainder_words):
        return "The sentence is composed of palindromes and every word is an anagram of each other."
    else:
        return "The sentence is composed of palindromes. However, the words are not anagrams of each other."