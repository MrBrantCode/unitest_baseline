"""
QUESTION:
Create a function `build_word_frequency` that takes two parameters: `input_string` and `stop_words`. The function should return a dictionary where the keys are the words in the `input_string` (after converting to lowercase and removing punctuation) and the values are their respective frequencies, excluding any stop words provided in the `stop_words` list. If the `input_string` is empty or contains only punctuation marks, the function should return an error message.
"""

import string

def build_word_frequency(input_string, stop_words):
    if not input_string or input_string.strip(string.punctuation).strip() == '':
        return "Error: Input string is empty or contains only punctuation marks."
    
    input_string = input_string.lower().translate(str.maketrans('', '', string.punctuation))
    words = input_string.split()
    words = [word for word in words if word not in stop_words]
    
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    return word_freq