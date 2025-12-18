"""
QUESTION:
Create a function named `count_substrings` that takes a sentence as input and returns the number of substrings of length 3 that start with a vowel and end with a consonant. The function should be case-insensitive and consider only alphabets as vowels and consonants.
"""

def count_substrings(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    count = 0

    # Iterate through each character in the sentence
    for i in range(len(sentence) - 2):
        # Check if the current character is a vowel
        if sentence[i].lower() in vowels:
            # Check if the next character is a consonant
            if sentence[i+2].lower() in consonants:
                count += 1

    return count