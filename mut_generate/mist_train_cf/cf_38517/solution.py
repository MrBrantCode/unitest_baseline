"""
QUESTION:
Implement the `calculateNGramFrequency(text, n)` function, which takes a string `text` and an integer `n` as input, and returns a dictionary where the keys are the n-grams and the values are the frequency of each n-gram in the text. The n-grams are contiguous sequences of n items (words) from the input text.
"""

def calculateNGramFrequency(text, n):
    words = text.split()
    ngrams = [' '.join(words[i:i+n]) for i in range(len(words)-n+1)]
    frequency = {}
    for gram in ngrams:
        if gram in frequency:
            frequency[gram] += 1
        else:
            frequency[gram] = 1
    return frequency