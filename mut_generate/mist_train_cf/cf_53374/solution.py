"""
QUESTION:
Create a function named `WordFrequency` that takes a list of stop words as input. The function should be able to dynamically add or remove stop words from the list. It should also be able to count the frequency of individual words in a given text string, excluding the stop words, while considering the effects of capitalization and punctuation. The function should return a dictionary with words as keys and their frequencies as values. The approach should be memory efficient.
"""

import string
from collections import Counter, defaultdict

def word_frequency(stop_words=None, text=None):
    stop_words = defaultdict(int) if stop_words is None else defaultdict(int, {word.lower(): 1 for word in stop_words})

    def add_stop_word(word):
        stop_words[word.lower()] = 1

    def remove_stop_word(word):
        if stop_words[word.lower()] == 1:
            del stop_words[word.lower()]

    def count_frequency(text):
        text = text.translate(str.maketrans('', '', string.punctuation)).lower()
        words = (word for word in text.split() if word.lower() not in stop_words)

        return Counter(words)

    # Dynamically add methods to word_frequency
    word_frequency.add_stop_word = add_stop_word
    word_frequency.remove_stop_word = remove_stop_word
    word_frequency.count_frequency = count_frequency

    return word_frequency


# Example usage (maintained for clarity, though not requested)
wf = word_frequency(['the', 'a', 'in'])
text = "In a land far far away, in the midst of thick forests and tall mountains."
print(wf.count_frequency(text))

wf.add_stop_word('and')
print(wf.count_frequency(text))

wf.remove_stop_word('the')
print(wf.count_frequency(text))