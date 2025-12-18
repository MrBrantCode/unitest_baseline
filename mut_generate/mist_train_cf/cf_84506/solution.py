"""
QUESTION:
Create a function named `filter_words` that takes three parameters: `word_list`, `vowels`, and `number_of_consonants`. This function should return a new list containing only the words from `word_list` that include at least one of the given `vowels` in consecutive order and have at least `number_of_consonants`.
"""

def filter_words(word_list, vowels, number_of_consonants):
    def contains_vowels(word, vowels):
        for vowel in vowels:
            if vowel in word:
                return True
        return False

    def consonant_count(word, number_of_consonants):
        consonant = 0
        for char in word:
            if char.lower() not in 'aeiou':
                consonant += 1
        return consonant >= number_of_consonants

    return [word for word in word_list if contains_vowels(word, vowels) and consonant_count(word, number_of_consonants)]