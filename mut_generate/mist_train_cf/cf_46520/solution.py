"""
QUESTION:
Design a function `find_extra_missing_words(sentence_a, sentence_b)` to find the words that are present in one sentence but not in another. The function should take two sentences as input, split them into individual words, and return the extra words in each sentence. The function should be case-sensitive and consider words with punctuation as different from the same words without punctuation. It should also ignore the order of words in the sentences and treat duplicates as a single word.
"""

def find_extra_missing_words(sentence_a, sentence_b):
    words_a = set(sentence_a.split())
    words_b = set(sentence_b.split())
    
    extra_in_a = words_a - words_b
    extra_in_b = words_b - words_a
    
    return extra_in_a, extra_in_b