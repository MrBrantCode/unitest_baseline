"""
QUESTION:
Write a function `get_closest_vowel(word)` that finds the nearest vowel situated between two consonants from the right side of the word (case sensitive). The function should ignore vowels at the beginning or end of the word and assume the input string contains only English letters. If no such vowel is found, the function should return an empty string.
"""

def get_closest_vowel(word):
    vowels = "AEIOUaeiou"
    candidate_vowels = []

    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels and word[i - 1] not in vowels and word[i + 1] not in vowels:
            candidate_vowels.append(word[i])

    return candidate_vowels[0] if candidate_vowels else ""