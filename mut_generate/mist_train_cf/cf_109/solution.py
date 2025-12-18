"""
QUESTION:
Create a function `sentiment_analysis` that classifies the sentiment of a given sentence as 'Positive sentiment', 'Negative sentiment', or 'Neutral sentiment' based on the presence of certain keywords, such as 'good' and 'bad'. The function should take a sentence as input and return the predicted sentiment. The function should be able to handle multiple occurrences of 'good' and 'bad' in the sentence. 

The function should be optimized for efficiency and scalability, and should be able to handle large volumes of text data for sentiment analysis.
"""

def sentiment_analysis(sentence):
    words = sentence.split()
    positive_count = 0
    negative_count = 0

    for word in words:
        if word == 'good':
            positive_count += 1
        elif word == 'bad':
            negative_count += 1
        else:
            negative_count += 0

    if positive_count > negative_count:
        return 'Positive sentiment'
    elif positive_count < negative_count:
        return 'Negative sentiment'
    else:
        return 'Neutral sentiment'