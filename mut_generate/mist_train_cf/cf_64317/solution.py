"""
QUESTION:
Create a function called `find_anagram_words` that takes two parameters, `sen1` and `sen2`, representing two distinct sentences. The function should be case-insensitive and treat words with the same characters but in different orders as the same word (anagrams). The function should return a dictionary where each key is a unique word/anagram and each value is the frequency of that word/anagram in both sentences. The function should ignore punctuation attached to words.
"""

import string

def find_anagram_words(sen1, sen2):
    sen1 = sen1.translate(str.maketrans('', '', string.punctuation)).lower().split()
    sen2 = sen2.translate(str.maketrans('', '', string.punctuation)).lower().split()
    
    anagram_words = {}
    
    for word in sen1:
        sorted_word = "".join(sorted(word))
        if sorted_word in anagram_words:
            anagram_words[sorted_word] += 1
        else:
            anagram_words[sorted_word] = 1
            
    for word in sen2:
        sorted_word = "".join(sorted(word))
        if sorted_word in anagram_words:
            anagram_words[sorted_word] += 1
        else:
            anagram_words[sorted_word] = 1
    
    return anagram_words