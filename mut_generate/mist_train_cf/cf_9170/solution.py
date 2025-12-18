"""
QUESTION:
Create a function `predict_subscription_plan` that takes a dictionary of purchase history where keys are product categories (e.g., 'shirts', 'hats', 'jeans') and values are the corresponding quantities purchased. The function should return the recommended subscription plan based on the purchase history. The subscription plans are as follows: 
- If the preferred category is 'shirts', recommend 'Shirt Lover'.
- If the preferred category is 'hats', recommend 'Hat Enthusiast'.
- If the preferred category is 'jeans', recommend 'Denim Obsessed'.
- If purchases are made from multiple categories, recommend 'Mix & Match'.
"""

def predict_subscription_plan(purchase_history):
    """
    This function predicts a customer's subscription plan based on their purchase history.
    
    Parameters:
    purchase_history (dict): A dictionary of product categories and their corresponding quantities purchased.
    
    Returns:
    str: The recommended subscription plan based on the customer's purchase history.
    """
    # Count the quantity of each product category purchased
    preferred_category = max(purchase_history, key=purchase_history.get)
    
    # Determine the customer's subscription plan based on their preferred product category
    if len(purchase_history) > 1:
        return 'Mix & Match'
    elif preferred_category == 'shirts':
        return 'Shirt Lover'
    elif preferred_category == 'hats':
        return 'Hat Enthusiast'
    elif preferred_category == 'jeans':
        return 'Denim Obsessed'
    else:
        return 'Unknown'