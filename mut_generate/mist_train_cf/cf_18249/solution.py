"""
QUESTION:
Create a function called `build_word_frequency_dict` that takes a string `input_string` and a list of stop words `stop_words` as input. The function should return a dictionary where the keys are the unique words in the input string (excluding punctuation and stop words) and the values are their respective frequencies. The function should ignore punctuation marks, convert all words to lowercase, and remove any stop words before counting the frequencies.
"""

import string

def build_word_frequency_dict(input_string, stop_words):
    word_freq_dict = {}
    input_string = input_string.translate(str.maketrans('', '', string.punctuation))
    input_string = input_string.lower()
    words = input_string.split()
    words = [word for word in words if word not in stop_words]
    for word in words:
        if word in word_freq_dict:
            word_freq_dict[word] += 1
        else:
            word_freq_dict[word] = 1
    return word_freq_dict