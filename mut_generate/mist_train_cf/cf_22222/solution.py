"""
QUESTION:
Implement the `get_second_highest_frequency_word` function to retrieve the word with the second highest frequency from a given text, considering word case sensitivity and excluding words that start with a vowel ('a', 'e', 'i', 'o', 'u'). The function should take a string `text` as input and return the word as a string or `None` if there is no second word.
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