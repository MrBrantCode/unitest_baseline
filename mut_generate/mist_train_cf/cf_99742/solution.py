"""
QUESTION:
Create a function named `remove_words` that takes two arguments: `dataset`, a list of sentences, and `words_to_remove`, a list of words to be removed from the sentences. The function should use regular expressions to remove the targeted words from the sentences, handling variations in grammar, word order, and cases where the targeted word is part of a larger word. The function should return the modified dataset with the targeted words removed from each sentence, and the replacement should be case-insensitive.
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