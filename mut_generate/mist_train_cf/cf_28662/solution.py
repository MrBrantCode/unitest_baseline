"""
QUESTION:
Write a function named `count_letter_frequencies` that takes a list of strings as input, counts the frequency of each letter in all the strings, and returns the result as a dictionary where the keys are the letters and the values are the frequencies of the letters. The function should be case-sensitive.
"""

def count_letter_frequencies(words):
    letter_freq = {}
    for word in words:
        for letter in word:
            if letter in letter_freq:
                letter_freq[letter] += 1
            else:
                letter_freq[letter] = 1
    return letter_freq