"""
QUESTION:
Write a function `count_substrings(sentence)` that counts the number of substrings of length 3 in the given sentence, where each substring starts with a vowel and ends with a consonant. The function should be case-insensitive, treating both lowercase and uppercase vowels and consonants as valid.
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