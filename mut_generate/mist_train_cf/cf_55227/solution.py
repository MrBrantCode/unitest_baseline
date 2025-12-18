"""
QUESTION:
Design a function called `count_consonants` that takes a list of sentences as input and returns the total number of consonants in the sentences that meet the following conditions:

- The sentence must not start with a vowel.
- The sentence must not end with a consonant.
- The sentence must not contain any numbers.
- The sentence must have at least 5 words.

Note that the function should be case-insensitive and should safely iterate over the list of sentences without skipping any elements.
"""

def count_consonants(sentences):
    total_consonants = 0
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

    for sentence in sentences:
        words = sentence.split()
        if words[0][0] in vowels or words[-1][-1] in consonants or len(words) < 5 or any(char.isdigit() for char in sentence):
            continue
        for word in words:
            for letter in word:
                if letter in consonants:
                    total_consonants += 1
    return total_consonants