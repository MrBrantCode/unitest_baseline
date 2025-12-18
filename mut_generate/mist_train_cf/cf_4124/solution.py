"""
QUESTION:
Write a function `extract_sentiment_adjectives` that takes a sentence as input and returns the sentiment label and a list of literal adjectives (ignoring metaphorical or figurative adjectives) used to describe the food in the sentence. The function should utilize the Stanford CoreNLP library in Python and use the Universal Dependencies (UD) annotation scheme for part-of-speech tags and dependency relations. The output should include the sentiment label (Positive, Negative, or Neutral) and a list of lowercase adjective words.
"""

def extract_sentiment_adjectives(sentence):
    sentiment = sentence.sentiment
    adjectives = []

    for word in sentence.words:
        if word.upos == 'ADJ' and word.deprel != 'amod' and word.deprel != 'advmod':
            adjectives.append(word.text.lower())

    return sentiment, adjectives