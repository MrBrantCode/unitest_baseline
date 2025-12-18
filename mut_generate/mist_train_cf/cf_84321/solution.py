"""
QUESTION:
Write a function `count_polysyllabic_words` that takes a string of words as input and returns the count of polysyllabic words and the actual polysyllabic words. A polysyllabic word is defined as a word containing at least one of each vowel (including 'y') and having at least two syllables, where a syllable is considered a vowel sequence. The function should handle upper-case, lower-case, and mixed-case strings without using any built-in or external libraries or modules.
"""

def count_polysyllabic_words(input_string):
    vowels = set("aeiouy")
    input_string = input_string.lower()
    words = input_string.split()
    polysyllabic_words = []
    count = 0

    for word in words:
        if vowels.issubset(word):
            syllables = sum(word[i] in vowels and word[i - 1] not in vowels for i in range(1, len(word)))
            if syllables > 1:
                polysyllabic_words.append(word)
                count += 1

    return count, polysyllabic_words