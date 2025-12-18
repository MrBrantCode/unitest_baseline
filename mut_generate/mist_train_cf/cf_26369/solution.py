"""
QUESTION:
Write a function `sentiment_analysis` that takes a string input representing a movie review and returns a string indicating the sentiment of the review, either "positive" or "negative".
"""

def sentiment_analysis(review):
    # assuming we have a dictionary with movie review sentiments
    sentiments = {
        "love": "positive",
        "like": "positive",
        "hate": "negative",
        "dislike": "negative"
    }
    
    # split the review into words
    words = review.split()
    
    # check each word in the review
    for word in words:
        # if the word is in our sentiments dictionary, return the sentiment
        if word in sentiments:
            return sentiments[word]
    
    # if no sentiment words are found, return "negative" by default
    return "negative"