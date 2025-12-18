"""
QUESTION:
Create a Python function `extract_features` that takes a list of words as input and returns a dictionary where each word is a key and the corresponding value is True. This function will be used to extract features from movie reviews. 

The input list of words will contain a movie review, and the function should return a dictionary where each word in the review is a key. The function should not contain any irrelevant information or operations. 

Restrictions: 
- The function should not take any other input other than a list of words.
- The function should return a dictionary.
- The function should not perform any Natural Language Processing operations other than creating a dictionary of words.
"""

def extract_features(word_list):
    return dict([(word, True) for word in word_list])