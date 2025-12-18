"""
QUESTION:
Write a function named `max_vowel_words` that takes a list of distinct English words as input. The function should return the word or words with the maximum quantity of vowel characters (a, e, i, o, u, y). If multiple words share the maximum quantity, return all of them.
"""

def max_vowel_words(word_list):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    max_vowel_count = 0
    max_vowel_words = []

    for word in word_list:
        vowel_count = sum(letter in vowels for letter in word)
        if vowel_count > max_vowel_count:
            max_vowel_count = vowel_count
            max_vowel_words = [word]
        elif vowel_count == max_vowel_count:
            max_vowel_words.append(word)

    return max_vowel_words