"""
QUESTION:
Create a function named `create_skip_bigrams` that takes two parameters: `sentence` (the input string from which to generate bigrams) and `window_size` (the maximum distance between words in the bigrams, defaulting to 2). The function should return a list of tuples, where each tuple represents a bigram of non-consecutive words in the sentence, up to the specified `window_size`.
"""

def create_skip_bigrams(sentence, window_size=2):
    tokens = sentence.split()
    bigrams = []
    for i in range(len(tokens)):
        for distance in range(1, window_size+1):
            if i+distance < len(tokens):
                bigrams.append((tokens[i], tokens[i+distance]))
    return bigrams