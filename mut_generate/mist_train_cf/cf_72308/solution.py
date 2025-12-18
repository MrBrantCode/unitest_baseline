"""
QUESTION:
Write a function `find_max_vowels` that takes a list of words as input and returns a tuple. The first element of the tuple is a list of words with the maximum number of vowels, and the second element is the ratio of vowels to total characters in those words. The function should be case-insensitive and ignore non-alphabet characters. If the input list is empty, the function should return `None` and 0.
"""

def find_max_vowels(words):
    if not words:
        return None, 0

    def count_vowels(word):
        v_count = 0
        counter = 0
        vowel = set('aeiouAEIOU')
        for character in word:
            if character.isalpha():
                counter += 1
                if character in vowel:
                    v_count += 1
        return v_count / counter if counter != 0 else 0

    max_vowels = count_vowels(words[0])
    max_vowel_words = [words[0]]
    for word in words[1:]:
        vowels = count_vowels(word)
        if vowels > max_vowels:
            max_vowels = vowels
            max_vowel_words = [word]
        elif vowels == max_vowels:
            max_vowel_words.append(word)
    return max_vowel_words, max_vowels