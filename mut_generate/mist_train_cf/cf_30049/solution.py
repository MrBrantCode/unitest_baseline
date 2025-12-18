"""
QUESTION:
Create a function `create_tri_gram_model` that takes a list of strings (`reuters_dataset`) as input, where each string represents a document. The function should return a Tri-gram language model represented as a dictionary of dictionaries. The outer dictionary keys are the first two words of the Tri-gram, and the inner dictionaries contain the third word of the Tri-gram and its frequency. The input documents can be split into words using spaces.
"""

from collections import defaultdict

def create_tri_gram_model(reuters_dataset):
    model = defaultdict(lambda: defaultdict(int))
    
    for document in reuters_dataset:
        words = document.split()
        for i in range(len(words) - 2):
            tri_gram = ' '.join(words[i:i+2])
            next_word = words[i+2]
            model[tri_gram][next_word] += 1
    
    return model