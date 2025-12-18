"""
QUESTION:
Write a function named `longest_word_ratio(sentence)` that takes a sentence as input, finds the longest word with at least two consecutive vowels, calculates the ratio of consonants to vowels in this word, and then returns the difference between this ratio and the average of the ratios for all words with at least two consecutive vowels. The function should return `None` if no words with consecutive vowels are found.
"""

def longest_word_ratio(sentence):
    words_with_vowels = []
    for word in sentence.split():
        if any(c in 'aeiou' for c in word):
            for i in range(len(word) - 1):
                if word[i] in 'aeiou' and word[i+1] in 'aeiou':
                    words_with_vowels.append(word)
                    break
    if not words_with_vowels:
        return None
    longest_word = max(words_with_vowels, key=len)
    consonants = sum(1 for c in longest_word if c.isalpha() and c not in 'aeiou')
    vowels = sum(1 for c in longest_word if c in 'aeiou')
    ratio = consonants / vowels
    avg_ratio = sum(sum(1 for c in word if c.isalpha() and c not in 'aeiou') / sum(1 for c in word if c in 'aeiou') for word in words_with_vowels) / len(words_with_vowels)
    return ratio - avg_ratio