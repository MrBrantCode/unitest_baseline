"""
QUESTION:
Implement the function `get_most_common_phrase(strings)` that takes a list of strings as input, and returns the most common phrase that meets the following conditions:

* The phrase contains at least three words.
* The phrase starts with a capital letter.
* The phrase ends with a punctuation mark.
* The phrase has a length of at least 10 characters.
* The phrase does not include any numbers or special characters.
* The phrase is not a common English phrase such as "I love you" or "Hello world".
* The returned phrase is in all uppercase letters.

If there are no eligible phrases, the function should return `None`.
"""

import re
from collections import Counter

def get_most_common_phrase(strings):
    pattern = r'[A-Z][^.!?]*[.!?]'
    combined_string = ' '.join(strings)
    phrases = re.findall(pattern, combined_string)
    filtered_phrases = [phrase.upper() for phrase in phrases if len(phrase) >= 10 and not any(char.isdigit() or not char.isalnum() for char in phrase)]
    phrase_counts = Counter(filtered_phrases)
    excluded_phrases = ['I LOVE YOU', 'HELLO WORLD']  
    for phrase in excluded_phrases:
        phrase_counts.pop(phrase, None)
    most_common_phrase = phrase_counts.most_common(1)
    if most_common_phrase:
        return most_common_phrase[0][0]
    else:
        return None