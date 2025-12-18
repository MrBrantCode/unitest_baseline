"""
QUESTION:
Implement a function `predict_probability` that takes in a dictionary of features of a house and a trained model as input and returns the probability of the house being sold for above $200,000. Assume that the model is already trained and provided. The function should use the model to predict the probability based on the given features.
"""

def predict_probability(features, model):
    """
    This function receives features of a house and a trained model,
    and returns the probability of the house being sold for above $200k.
    
    :param features: dict, features of a house e.g. {'size': 2300, 'rooms': 3, 'age': 10, 'location': 'downtown'}
    :param model: trained model
    :return: probability of the house being sold for more than $200k
    """
    return model.predict_proba([features])[0][1]