"""
QUESTION:
Write a function `get_second_highest_frequency_word(text)` that takes a string `text` as input and returns the word with the second highest frequency. The function should be case sensitive and exclude words that start with a vowel. If there is no second word, the function should return `None`.
"""

from collections import defaultdict

def get_second_highest_frequency_word(text):
    words = text.split()
    frequency = defaultdict(int)

    vowels = ['a', 'e', 'i', 'o', 'u']

    for word in words:
        if word[0].lower() not in vowels:
            frequency[word] += 1

    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    # Ensure there is at least a second word
    if len(sorted_frequency) > 1:
        return sorted_frequency[1][0]

    return None