"""
QUESTION:
Determine the emotional sentiment of a given language expression and provide a justification for the inference based on the language cues used.

Function name: Determine Sentiment and Justification

Input: A string representing the language expression.

Restrictions: Output a sentiment as either 'Negative' or 'Affirmative' and provide a clear justification for the inference.
"""

def Determine_Sentiment_and_Justification(expression):
    """
    Determine the emotional sentiment of a given language expression and provide a justification for the inference based on the language cues used.

    Args:
        expression (str): A string representing the language expression.

    Returns:
        tuple: A tuple containing the sentiment as either 'Negative' or 'Affirmative' and a clear justification for the inference.
    """
    # Define a dictionary to map negative words to their corresponding justifications
    negative_words = {
        'disaster': 'directly indicates a strong negative sentiment as it is typically used to describe something that has gone very wrong or has not achieved its intended purpose or expectation',
        'hate': 'directly indicates a strong negative sentiment as it is typically used to describe a strong feeling of dislike or hostility towards something',
        # Add more words and justifications as needed
    }

    # Define a dictionary to map affirmative words to their corresponding justifications
    affirmative_words = {
        'love': 'directly indicates a strong affirmative sentiment as it is typically used to describe a strong feeling of affection or fondness towards something',
        'great': 'directly indicates a strong affirmative sentiment as it is typically used to describe something that is of exceptionally high quality or excellence',
        # Add more words and justifications as needed
    }

    # Split the expression into words
    words = expression.split()

    # Initialize sentiment and justification variables
    sentiment = None
    justification = None

    # Check for negative words
    for word in words:
        if word.lower() in negative_words:
            sentiment = 'Negative'
            justification = negative_words[word.lower()]
            break

    # Check for affirmative words
    if sentiment is None:
        for word in words:
            if word.lower() in affirmative_words:
                sentiment = 'Affirmative'
                justification = affirmative_words[word.lower()]
                break

    # If no sentiment is found, return a default justification
    if sentiment is None:
        sentiment = 'Neutral'
        justification = 'No clear sentiment can be inferred from the expression.'

    return sentiment, justification