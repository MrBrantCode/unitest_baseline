"""
QUESTION:
Create a function called `vowel_count` that takes a sentence as input and returns a key to sort sentences in descending order, first by the number of vowels in each sentence and then by the index of the first occurrence of a vowel in each sentence. The function should be case-insensitive and consider both lowercase and uppercase vowels as the same.
"""

def vowel_count(sentence):
    vowels = "aeiou"
    # Count the number of vowels
    vowel_count = sum(1 for char in sentence.lower() if char in vowels)
    # Find the first occurrence of each vowel
    first_vowel_index = min((sentence.lower().find(vowel) for vowel in vowels if vowel in sentence.lower()), default=len(sentence))
    return -vowel_count, first_vowel_index