"""
QUESTION:
Analyze a given text to determine its sentiment. The function should indicate whether the sentiment is positive or negative.
"""

def analyze_sentiment(text):
    # Initialize a dictionary of positive and negative words
    positive_words = ["amazing", "happy", "good", "great", "excellent"]
    negative_words = ["bad", "sad", "terrible", "awful", "poor"]
    
    # Convert the text to lowercase and split it into words
    words = text.lower().split()
    
    # Initialize counters for positive and negative words
    positive_count = 0
    negative_count = 0
    
    # Count the number of positive and negative words in the text
    for word in words:
        if word in positive_words:
            positive_count += 1
        elif word in negative_words:
            negative_count += 1
    
    # Determine the sentiment based on the word counts
    if positive_count > negative_count:
        return "positive"
    elif negative_count > positive_count:
        return "negative"
    else:
        return "neutral"