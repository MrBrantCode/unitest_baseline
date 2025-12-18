"""
QUESTION:
Create a function `find_anagrams` that takes a list of words as input and returns a dictionary where the keys are words and the values are lists of their anagram pairs. The function should ignore case, remove non-alphabetic characters, and omit non-alphabetic strings from the input list. It should also exclude any words that do not have at least one anagram pair.
"""

def find_anagrams(words):
    anagrams = {}

    for word in words:
        sanitized_word = "".join(char for char in word.lower() if char.isalpha())

        if sanitized_word:
            sorted_word = "".join(sorted(sanitized_word))

            if sorted_word in anagrams:
                if word not in anagrams[sorted_word]:
                    anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]

    anagrams = {key: value for key, value in anagrams.items() if len(value) > 1}

    return anagrams