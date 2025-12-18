"""
QUESTION:
Create a function `sentiment_analysis` that takes a string of text as input and classifies it into either 'positive' or 'negative' sentiment based on the presence of profanity, hate speech, or other indicators of negative evaluation, without considering neutral or mixed sentiment cases.
"""

def sentiment_analysis(text):
    # Initialize a list of negative words
    negative_words = ["hate", "bad", "awful", "terrible", "vulgar", "offensive", "worst"]
    
    # Convert the text to lowercase
    text = text.lower()
    
    # Check if any negative word is present in the text
    if any(word in text for word in negative_words):
        return 'negative'
    else:
        return 'positive'