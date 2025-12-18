"""
QUESTION:
Design a function named 'count_consonants' that takes a list of sentences as input, filters out the sentences that do not meet certain conditions, and returns the total count of consonants in the remaining sentences. 

The function should discard sentences that start with a vowel (both lowercase and uppercase), end with a consonant (both lowercase and uppercase), contain any special characters or numbers, have less than 5 words, or have more than 10 words. The function should handle case sensitivity and only count consonants (both lowercase and uppercase).
"""

def count_consonants(sentences):
    total_consonants = 0
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'aeiouAEIOU'
    filtered_sentences = [sentence for sentence in sentences if all(
        letter.isalpha() for word in sentence.split() for letter in word
    ) and sentence[0] not in vowels and sentence[-1] not in consonants and 5 <= len(sentence.split()) <= 10]
    for sentence in filtered_sentences:
        total_consonants += sum(1 for word in sentence for letter in word if letter in consonants)
    return total_consonants