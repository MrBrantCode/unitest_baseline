"""
QUESTION:
Create a function called `classify_data` that takes in a list of words and classifies them into two categories: Positive or Negative. The function should consider 'good', 'excellent', and 'high quality' as Positive, and 'bad', 'poor', and 'mediocre' as Negative. The function should return two lists, one for Positive data and one for Negative data.
"""

def classify_data(data):
    """
    Classify the input data into two categories: Positive or Negative.

    Args:
        data (list): A list of words to be classified.

    Returns:
        tuple: Two lists, one for Positive data and one for Negative data.
    """
    # Define the positive and negative words
    positive_words = ['good', 'excellent', 'high quality']
    negative_words = ['bad', 'poor', 'mediocre']

    # Initialize empty lists to store positive and negative words
    positive_data = []
    negative_data = []

    # Classify the words
    for word in data:
        if word in positive_words:
            positive_data.append(word)
        elif word in negative_words:
            negative_data.append(word)

    return positive_data, negative_data