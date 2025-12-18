"""
QUESTION:
Write a function `longest_word_ratio(sentence)` that takes a sentence as input and returns the difference between the ratio of consonants to vowels in the longest word with at least two consecutive vowels and the average of the ratios for all words with at least two consecutive vowels in the sentence. If no words contain at least two consecutive vowels, return None.
"""

def longest_word_ratio(sentence):
    words_with_vowels = []
    for word in sentence.split():
        if any(c in 'aeiou' for c in word.lower()):
            for i in range(len(word) - 1):
                if word[i].lower() in 'aeiou' and word[i+1].lower() in 'aeiou':
                    words_with_vowels.append(word)
                    break
    if not words_with_vowels:
        return None
    longest_word = max(words_with_vowels, key=len)
    consonants = sum(1 for c in longest_word if c.isalpha() and c.lower() not in 'aeiou')
    vowels = sum(1 for c in longest_word if c.lower() in 'aeiou')
    ratio = consonants / vowels
    avg_ratio = sum(sum(1 for c in word if c.isalpha() and c.lower() not in 'aeiou') / sum(1 for c in word if c.lower() in 'aeiou') for word in words_with_vowels) / len(words_with_vowels)
    return ratio - avg_ratio