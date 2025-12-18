"""
QUESTION:
Write a function `predict_price` that predicts the optimal price for a product based on user input using a trained Linear Regression model. The function takes the trained model and a 2D array `user_input` representing the product details as input. The function returns the predicted optimal price. Assume that the model has been trained on a dataset where the target variable is 'price' and the features are the other columns.
"""

def predict_price(model, user_input):
    """
    Predict the optimal price for a product based on user input using a trained Linear Regression model.

    Parameters:
    model (LinearRegression): A trained Linear Regression model.
    user_input (2D array): A 2D array representing the product details.

    Returns:
    predicted_price (float): The predicted optimal price.
    """
    predicted_price = model.predict(user_input)
    return predicted_price