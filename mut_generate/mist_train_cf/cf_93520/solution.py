"""
QUESTION:
Create a function named `classify_sentence(sentence)` that classifies a given sentence as "Positive", "Negative", or "Neutral" based on the sentiment of its individual words. The function should use two predefined lists: `positive_words` and `negative_words`, to determine the sentiment score of the sentence. The sentiment score should be incremented for each positive word and decremented for each negative word. The sentence should be classified as "Positive" if the sentiment score is greater than zero, "Negative" if it is less than zero, and "Neutral" if it is zero or close to zero.
"""

def classify_sentence(sentence):
    positive_words = ['good', 'happy', 'great', 'awesome', 'excellent']
    negative_words = ['bad', 'sad', 'terrible', 'awful', 'horrible']
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