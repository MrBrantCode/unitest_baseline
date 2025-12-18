"""
QUESTION:
Create a function `categorize_weather_sentence(sentence)` that categorizes a given sentence into one of four weather description categories: 
- Positive Weather Description 
- Negative Weather Description 
- Neutral Weather Description 
- Weather Description with Emotion

The function should take a sentence as input and return the corresponding category. The sentence can contain various words and phrases that express emotions or describe weather conditions.
"""

def categorize_weather_sentence(sentence):
    """
    Categorize a given sentence into one of four weather description categories:
    - Positive Weather Description 
    - Negative Weather Description 
    - Neutral Weather Description 
    - Weather Description with Emotion

    Args:
        sentence (str): The input sentence to be categorized.

    Returns:
        str: The category of the input sentence.
    """
    
    # Define positive and negative words
    positive_words = ["sunny", "clear", "beautiful", "warm", "nice", "good", "lovely", "pleasant"]
    negative_words = ["rainy", "cloudy", "stormy", "cold", "bad", "awful", "terrible", "unpleasant"]
    emotional_words = ["love", "hate", "like", "dislike", "enjoy", "scared", "happy", "sad"]

    # Convert the sentence to lowercase for case-insensitive comparison
    sentence = sentence.lower()

    # Check for emotional words
    if any(emotional_word in sentence for emotional_word in emotional_words):
        return "Weather Description with Emotion"

    # Check for positive words
    if any(positive_word in sentence for positive_word in positive_words):
        return "Positive Weather Description"

    # Check for negative words
    if any(negative_word in sentence for negative_word in negative_words):
        return "Negative Weather Description"

    # If no specific words are found, categorize as neutral
    return "Neutral Weather Description"