"""
QUESTION:
Implement a function `extract_features` that takes a list of words as input and returns a dictionary where the keys are the words and the values are all `True`. 

Restrictions: 
- The function should be used to extract features from a list of words for a sentiment analysis model.
"""

def extract_features(words):
    return dict([(word, True) for word in words])