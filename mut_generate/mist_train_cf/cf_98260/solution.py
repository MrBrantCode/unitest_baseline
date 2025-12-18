"""
QUESTION:
Create a function `remove_words` that takes two parameters: a list of sentences `dataset` and a list of words to delete `words_to_remove`. The function should return the modified `dataset` with all occurrences of `words_to_remove` deleted from each sentence, considering variations in grammar, word order, and cases where the targeted word is part of a larger word. The function should also handle cases where the targeted word is at the beginning, end, or middle of a sentence and is surrounded by different characters, and should be case-insensitive.
"""

import re

def remove_words(dataset, words_to_remove):
    for i in range(len(dataset)):
        sentence = dataset[i]
        for word in words_to_remove:
            sentence = re.sub(r'\b{}\b'.format(word), '', sentence, flags=re.IGNORECASE)
            sentence = re.sub(r'^{}\b'.format(word), '', sentence, flags=re.IGNORECASE)
            sentence = re.sub(r'\b{}$'.format(word), '', sentence, flags=re.IGNORECASE)
            sentence = re.sub(r'\W{}\W'.format(word), '', sentence, flags=re.IGNORECASE)
        dataset[i] = sentence
    return dataset