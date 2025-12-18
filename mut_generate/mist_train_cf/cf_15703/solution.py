"""
QUESTION:
Implement a function `sentiment_analysis` that takes a text as input and returns a sentiment analysis of the text. The function should consider negative keywords and phrases, context, and reviewer's credibility to calculate the overall sentiment score. It should also identify key factors contributing to the sentiment.
"""

def sentiment_analysis(text):
    """
    This function performs sentiment analysis on the input text.
    
    Parameters:
    text (str): The input text for sentiment analysis.
    
    Returns:
    dict: A dictionary containing the sentiment score and key factors contributing to the sentiment.
    """

    # Define negative keywords and phrases
    negative_keywords = ["total disaster", "complete waste of time", "poor acting", "weak plot", "subpar special effects", 
                        "lack of character development", "meaningless dialogue", "excessive use of clichés", "predictable twists"]

    # Initialize sentiment score and key factors
    sentiment_score = 0
    key_factors = []

    # Calculate sentiment score based on negative keywords and phrases
    for keyword in negative_keywords:
        if keyword in text.lower():
            sentiment_score -= 1
            key_factors.append(keyword)

    # Consider context and reviewer's credibility
    # For simplicity, this example does not include a credibility score, but it could be added as a parameter
    credibility_score = 1  # Replace with actual credibility score

    # Adjust sentiment score based on credibility
    sentiment_score *= credibility_score

    # Return sentiment score and key factors
    return {"sentiment_score": sentiment_score, "key_factors": key_factors}