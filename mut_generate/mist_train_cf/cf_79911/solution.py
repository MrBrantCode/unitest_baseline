"""
QUESTION:
Write a function named `get_first_consonant_flanked_vowel` that takes a string `word` as input, and returns the first vowel from the left that is flanked by consonants. Do not consider vowels at the start or end of the word. Return an empty string if no such vowel is found. The input string must only contain English characters.
"""

def get_first_consonant_flanked_vowel(word):
    """Given a word, find the first vowel that is enclosed by consonants from the left side of the word (case sensitive). Do not include vowels at the initiation or cessation of the word. Return an empty string if no such vowel found. The input string must only have English characters."""
    vowels = 'AEIOUaeiou'
    for i in range(1, len(word) - 1):  # Skip first and last characters
        if word[i] in vowels and word[i - 1] not in vowels:
            return word[i]
    
    return ""  # Return empty string if no vowel found