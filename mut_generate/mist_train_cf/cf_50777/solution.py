"""
QUESTION:
Create a function `select_phrases(s, n, m)` that takes a string `s`, a consonant count `n`, and a vowel count `m` as input. The function should return a list of phrases from the input string `s` where each phrase has a total consonant count of `n` and a total vowel count of `m`. If two consecutive phrases have the same consonant and vowel counts, they should be combined into a single phrase. If the string `s` is empty, the function should return an empty list. After merging two phrases, one consonant and one vowel should be randomly removed from the merged phrase. The input string `s` is guaranteed to contain only alphabets and spaces.
"""

def select_phrases(s, n, m):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    
    if not s:
        return []

    phrases_with_required_counts = []
    current_phrase = []
    current_consonants = 0
    current_vowels = 0

    for word in s.split():
        word_cons = len([ch for ch in word.lower() if ch in consonants])
        word_vows = len([ch for ch in word.lower() if ch in vowels])

        if (current_consonants + word_cons == n) and (current_vowels + word_vows == m):
            current_phrase.append(word)
            phrases_with_required_counts.append(' '.join(current_phrase))
            current_phrase = []
            current_consonants = 0
            current_vowels = 0

        elif (current_consonants + word_cons > n) or (current_vowels + word_vows > m):
            current_phrase = [word]
            current_consonants = word_cons
            current_vowels = word_vows

        else:
            current_phrase.append(word)
            current_consonants += word_cons
            current_vowels += word_vows

    return phrases_with_required_counts