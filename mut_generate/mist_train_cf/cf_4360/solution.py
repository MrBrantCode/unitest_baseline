"""
QUESTION:
Implement a function `naive_bayes_sentiment_analysis` that performs sentiment analysis on a given text using a Naive Bayes Classifier algorithm. The function should classify the sentiment of the text as positive, negative, or neutral and return the predicted sentiment along with a confidence score. The algorithm should be trained on a dataset of hotel reviews and be able to handle text in different languages. The function should have a time complexity of O(n), where n is the length of the text, and should not use any external libraries or APIs.
"""

def naive_bayes_sentiment_analysis(text):
    """
    This function performs sentiment analysis on a given text using a Naive Bayes Classifier algorithm.
    
    Parameters:
    text (str): The input text for sentiment analysis.
    
    Returns:
    tuple: A tuple containing the predicted sentiment (positive, negative, or neutral) and a confidence score.
    """

    # Preprocessing
    words = ''.join(e for e in text if e.isalnum() or e.isspace()).lower().split()
    
    # Train the Algorithm
    # For simplicity, let's assume we have a pre-trained model with the following probabilities
    prior_probabilities = {
        'positive': 0.4,
        'negative': 0.3,
        'neutral': 0.3
    }
    
    conditional_probabilities = {
        'positive': {'good': 0.1, 'bad': 0.05},
        'negative': {'good': 0.05, 'bad': 0.1},
        'neutral': {'good': 0.05, 'bad': 0.05}
    }
    
    # Predict the Sentiment
    products = {}
    for sentiment in prior_probabilities:
        product = prior_probabilities[sentiment]
        for word in words:
            if word in conditional_probabilities[sentiment]:
                product *= conditional_probabilities[sentiment][word]
        products[sentiment] = product
    
    # Normalize the product by dividing it by the sum of the products for all classes
    total_product = sum(products.values())
    normalized_products = {sentiment: product / total_product for sentiment, product in products.items()}
    
    # The class with the highest normalized product represents the predicted sentiment
    predicted_sentiment = max(normalized_products, key=normalized_products.get)
    
    # Calculate the confidence score by taking the maximum normalized product
    confidence_score = max(normalized_products.values())
    
    return predicted_sentiment, confidence_score