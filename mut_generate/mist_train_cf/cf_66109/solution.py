"""
QUESTION:
Construct a function named `count_consonants` that takes a list of sentences as input and returns the aggregate count of consonants from the sentences. The function should exclude sentences that start with a vowel, end with a consonant, contain numbers, special characters, or have fewer than 5 words. The function should also handle sentences with mixed case letters.
"""

def count_consonants(sentences):
    total_consonants = 0
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    
    for sentence in sentences:
        if (sentence[0].lower() not in consonants or sentence[-1].lower() in consonants or 
            len(sentence.split()) < 5 or any(char.isdigit() for char in sentence) or not sentence.isalpha()):
            continue
        words = sentence.lower().split()
        for word in words:
            for letter in word:
                if letter in consonants:
                    total_consonants += 1
    return total_consonants