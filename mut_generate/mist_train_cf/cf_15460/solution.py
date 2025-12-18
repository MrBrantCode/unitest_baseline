"""
QUESTION:
Predict the customer's subscription plan based on their purchase history of shirts, hats, and jeans.

Implement a function called "predict_subscription_plan" that takes in three non-negative integers representing the number of shirts, hats, and jeans purchased, and returns the predicted subscription plan. The function should follow these rules:
- Ultimate: more than 200 shirts or more than 100 hats
- Premium: more than 100 shirts or more than 50 hats
- Basic: less than or equal to 100 shirts and less than or equal to 50 hats
"""

def predict_subscription_plan(shirts, hats, jeans):
    if shirts > 200 or hats > 100:
        return "Ultimate"
    elif shirts > 100 or hats > 50:
        return "Premium"
    else:
        return "Basic"