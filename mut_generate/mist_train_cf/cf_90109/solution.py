"""
QUESTION:
Create a function named `count_consonants` that takes a string `sentence` as input and returns the total count of consonants in the sentence and the frequency of each consonant (including both lowercase and uppercase). The function should have a time complexity of O(n), where n is the length of the sentence, and a space complexity of O(1). Note that consonants are defined as letters 'bcdfghjklmnpqrstvwxyz' and their uppercase counterparts.
"""

def count_consonants(sentence):
    consonant_count = 0
    consonant_freq = {}
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')

    for char in sentence:
        if char in consonants:
            consonant_count += 1
            if char in consonant_freq:
                consonant_freq[char] += 1
            else:
                consonant_freq[char] = 1

    return consonant_count, consonant_freq