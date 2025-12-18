"""
QUESTION:
Create a function named `classify_sentence` that classifies a given sentence into one of five categories based on its sentiment and topic, with the categories being "Negative Sports Sentiment", "Positive Sports Sentiment", "Negative Non-Sports Sentiment", "Positive Non-Sports Sentiment", and "Neutral".
"""

def classify_sentence(sentence):
    # Define the list of sports-related words
    sports_words = ["football", "soccer", "basketball", "baseball", "tennis", "golf", "hockey", "rugby", "cricket", "volleyball"]
    
    # Initialize the sentiment score
    sentiment_score = 0
    
    # Calculate the sentiment score
    if "good" in sentence or "great" in sentence or "excellent" in sentence:
        sentiment_score += 1
    elif "bad" in sentence or "terrible" in sentence or "awful" in sentence:
        sentiment_score -= 1
    
    # Initialize the category
    category = ""
    
    # Check if the sentence contains any sports-related words
    if any(word in sentence.lower() for word in sports_words):
        # Classify the sentence as sports-related
        if sentiment_score > 0:
            category = "Positive Sports Sentiment"
        elif sentiment_score < 0:
            category = "Negative Sports Sentiment"
        else:
            category = "Neutral Sports Sentiment"
    else:
        # Classify the sentence as non-sports-related
        if sentiment_score > 0:
            category = "Positive Non-Sports Sentiment"
        elif sentiment_score < 0:
            category = "Negative Non-Sports Sentiment"
        else:
            category = "Neutral Sentiment"
    
    return category