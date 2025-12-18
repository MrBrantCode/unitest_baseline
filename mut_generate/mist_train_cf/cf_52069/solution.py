"""
QUESTION:
Design a function `detect_sentiment(sentence)` to detect the sentiment of a given sentence using natural language processing. The function should be able to handle negation and sarcasm in the sentence. The function should return 'Positive', 'Negative', 'Neutral', or 'Sarcasm'. Assume that negation is formed with words like 'not', 'isn't', 'wasn't', 'aren't', 'weren't' and sarcasm is formed by starting the sentence with 'Oh,'.
"""

import re

def detect_sentiment(sentence):
    
    positive_words = ['great', 'good', 'fantastic', 'excellent']
    negations = ['not', 'isn\'t', 'wasn\'t', 'aren\'t', 'weren\'t']
    sarcasm_indicator = 'oh,'

    # check for sarcasm
    if sentence.lower().startswith(sarcasm_indicator):
        return 'Sarcasm'

    # check for negations
    negation_in_sentence = any(re.search(f'\\b{neg}\\b', sentence.lower()) for neg in negations)
    positive_in_sentence = any(re.search(f'\\b{pos}\\b', sentence.lower()) for pos in positive_words)
    
    if negation_in_sentence and positive_in_sentence:
        return 'Negative'
    elif not negation_in_sentence and positive_in_sentence:
        return 'Positive'
    else:
        return 'Neutral'