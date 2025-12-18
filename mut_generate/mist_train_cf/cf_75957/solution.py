"""
QUESTION:
Implement a function `predict_user_rating` to predict a user's rating for an item using linear regression, where the input features are user attributes, item attributes, or a combination of both. The function should take in user attributes, item attributes, and the trained model coefficients as input, and return the predicted rating.
"""

def predict_user_rating(user_attributes, item_attributes, model_coefficients):
    """
    Predict a user's rating for an item using linear regression.

    Parameters:
    user_attributes (list): Attributes of the user.
    item_attributes (list): Attributes of the item.
    model_coefficients (list): Trained model coefficients.

    Returns:
    float: The predicted rating.
    """
    # Combine user and item attributes
    combined_attributes = user_attributes + item_attributes
    
    # Calculate the predicted rating using the linear regression formula
    predicted_rating = sum(attribute * coefficient for attribute, coefficient in zip(combined_attributes, model_coefficients))
    
    return predicted_rating