"""
QUESTION:
Create a function named `classify_sentence` that takes a sentence as input and returns its sentiment classification ("Positive", "Negative", or "Neutral") based on the sentiment of each individual word in the sentence. The function should use two predefined lists of positive and negative words to calculate an overall sentiment score. A positive sentiment score indicates a positive sentence, a negative sentiment score indicates a negative sentence, and a score close to zero indicates a neutral sentence.
"""

positive_words = ['good', 'happy', 'great', 'awesome', 'excellent']
negative_words = ['bad', 'sad', 'terrible', 'awful', 'horrible']

def classify_sentence(sentence):
    sentiment_score = 0
    
    # Tokenize the sentence
    words = sentence.split()
    
    # Iterate through each word
    for word in words:
        # Check if the word is positive
        if word in positive_words:
            sentiment_score += 1
        # Check if the word is negative
        elif word in negative_words:
            sentiment_score -= 1
    
    # Classify the sentence based on the sentiment score
    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Neutral"