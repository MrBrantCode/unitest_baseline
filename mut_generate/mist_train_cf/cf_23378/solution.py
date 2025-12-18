"""
QUESTION:
Predict the customer's subscription plan based on their purchase history. Given a customer's purchase history, including the type and quantity of items purchased, write a function called `predict_subscription_plan` to calculate the most likely subscription plan for the customer. The function should consider various factors such as item types and quantity of items purchased.
"""

def predict_subscription_plan(purchase_history):
    """
    Predicts the customer's subscription plan based on their purchase history.

    Args:
    purchase_history (dict): A dictionary containing the customer's purchase history.
        The keys are the item types and the values are the quantities purchased.

    Returns:
    str: The most likely subscription plan for the customer.
    """

    # Initialize a dictionary to store the weights for each factor
    weights = {
        'item_type': 0.4,
        'quantity': 0.3,
        'time_since_purchase': 0.2,
        'cost': 0.1
    }

    # Calculate the score for each factor
    item_type_score = sum([1 for item in purchase_history.keys() if item == 'premium'])
    quantity_score = sum(purchase_history.values())
    time_since_purchase_score = 1  # Assuming the time since purchase is not provided
    cost_score = sum([10 for item in purchase_history.keys() if item == 'premium'])

    # Calculate the total score
    total_score = (weights['item_type'] * item_type_score +
                   weights['quantity'] * quantity_score +
                   weights['time_since_purchase'] * time_since_purchase_score +
                   weights['cost'] * cost_score)

    # Determine the subscription plan based on the total score
    if total_score > 10:
        return 'Premium'
    elif total_score > 5:
        return 'Basic'
    else:
        return 'Free'