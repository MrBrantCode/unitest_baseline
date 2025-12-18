"""
QUESTION:
Construct a function named `vowel_count` that takes a string `sentence` as input and returns a dictionary where keys are unique words from the sentence, ignoring punctuation, and values represent the count of vocalic sounds in each word. If a word appears multiple times in the sentence, consider the second instance of the duplicate word. The function should handle English vowels only.
"""

import re
import collections
import string

def vowel_count(sentence):
    sentence = re.sub('['+string.punctuation+']', '', sentence).split()
    sentence.reverse()
    vowel_map = collections.OrderedDict()
    for word in sentence:
        if word not in vowel_map:
            vowel_map[word] = sum(1 for c in word if c in 'aeiouAEIOU')
    return collections.OrderedDict(reversed(list(vowel_map.items())))