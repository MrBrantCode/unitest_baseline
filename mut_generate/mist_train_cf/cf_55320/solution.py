"""
QUESTION:
Implement a function `reduce_unknown_confidence` that helps to reduce the high softmax probability of a neural network model when it predicts unknown or new data. The model is trained for multi-class image classification with a softmax activation function in the final layer.
"""

def reduce_unknown_confidence(softmax_probabilities, threshold):
    """
    Reduces the high softmax probability of a neural network model when it predicts unknown or new data.
    
    Args:
    softmax_probabilities (list): A list of softmax probabilities.
    threshold (float): The minimum probability required to classify an image as known.
    
    Returns:
    list: A list of adjusted softmax probabilities or 'unknown' if none of the output probabilities exceed the threshold.
    """
    
    # Check if none of the output probabilities exceed the threshold
    if all(prob < threshold for prob in softmax_probabilities):
        return 'unknown'
    
    # If at least one probability exceeds the threshold, return the original probabilities
    else:
        return softmax_probabilities