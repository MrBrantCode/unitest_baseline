"""
QUESTION:
Implement a function called `sentiment_analysis` to classify the sentiment of an article as positive, negative, or neutral, without using pre-trained models or libraries. The function should take an article as input and return its corresponding sentiment classification. The article contains text describing a topic, and the sentiment analysis should consider the context and potential negation of words to produce accurate results.
"""

def sentiment_analysis(article):
    """
    Classify the sentiment of an article as positive, negative, or neutral.

    Args:
        article (str): The article text to be analyzed.

    Returns:
        str: The sentiment classification of the article ('positive', 'negative', or 'neutral').
    """

    # Convert article into lowercase
    article = article.lower()
    
    # Define lists of positive and negative words
    positive_words = ['happy', 'good', 'great']
    negative_words = ['sad', 'bad', 'terrible']
    
    # Initialize sentiment score
    sentiment_score = 0
    
    # Check for negation words
    negation_words = ['not', 'no', 'never']
    negation_flag = False
    
    # Split article into words
    words = article.split()
    
    for i in range(len(words)):
        # Check for negation words
        if words[i] in negation_words:
            negation_flag = True
        # Check for positive words
        elif words[i] in positive_words:
            if negation_flag:
                sentiment_score -= 1
            else:
                sentiment_score += 1
            negation_flag = False
        # Check for negative words
        elif words[i] in negative_words:
            if negation_flag:
                sentiment_score += 1
            else:
                sentiment_score -= 1
            negation_flag = False
    
    # Classify sentiment based on the sentiment score
    if sentiment_score > 0:
        return 'positive'
    elif sentiment_score < 0:
        return 'negative'
    else:
        return 'neutral'