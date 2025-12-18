"""
QUESTION:
Construct two functions: `find_vowel_word` and `find_duplicate_vowels`, each taking a list of strings as input. The `find_vowel_word` function should return the first word that contains all the vowels (both upper and lower case). The `find_duplicate_vowels` function should return the first word that contains repeating vowels. If no word meets the desired conditions, return an empty string.
"""

def find_vowel_word(words):
    def contains_all_vowels(word):
        vowels = "aeiouAEIOU"
        return all(vowel in word for vowel in vowels)

    for word in words:
        if contains_all_vowels(word):
            return word
    return ""

def find_duplicate_vowels(words):
    def has_repeating_vowels(word):
        vowels = "aeiouAEIOU"
        return any(word.lower().count(vowel) > 1 for vowel in vowels)

    for word in words:
        if has_repeating_vowels(word):
            return word
    return ""