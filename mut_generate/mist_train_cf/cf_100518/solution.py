"""
QUESTION:
Write a function called `calculate_weightage` that classifies each sentence in a given paragraph into "optimistic" or "pessimistic" based on the presence of optimistic or pessimistic words. The function should use a pre-defined list of optimistic and pessimistic words, and calculate the weightage of each word based on its position in the sentence. The function should return the classification of each sentence along with the weightage of each word in a dictionary. The classification should be based on the following rules: 

- If the weightage is greater than 0, the sentence is classified as "optimistic".
- If the weightage is less than 0, the sentence is classified as "pessimistic".
- If the weightage is equal to 0, the sentence is classified as "neutral".

The function should also handle cases where a sentence contains both optimistic and pessimistic words. The weightage of each word should be calculated based on its position in the sentence, with words at the beginning of the sentence having a higher weightage than words at the end.
"""

import re

def calculate_weightage(sentence, optimistic_words, pessimistic_words):
    words = re.findall(r'\b\w+\b', sentence) # Extract all words from the sentence
    weightage = 0
    sentiment_scores = {}
    for i, word in enumerate(words):
        if word in optimistic_words:
            weightage += (len(words) - i) / len(words) # Weight the word based on its position
            if word in sentiment_scores:
                sentiment_scores[word] += weightage # Update the sentiment score of the word
            else:
                sentiment_scores[word] = weightage # Add the word to the dictionary with its sentiment score
        elif word in pessimistic_words:
            weightage -= (len(words) - i) / len(words) # Weight the word based on its position
            if word in sentiment_scores:
                sentiment_scores[word] += weightage # Update the sentiment score of the word
            else:
                sentiment_scores[word] = weightage # Add the word to the dictionary with its sentiment score
    if weightage > 0:
        classification = "optimistic"
    elif weightage < 0:
        classification = "pessimistic"
    else:
        classification = "neutral"
    return {"sentence": sentence, "classification": classification, "weightage": weightage, "sentiment_scores": sentiment_scores}