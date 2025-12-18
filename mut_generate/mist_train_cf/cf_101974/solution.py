"""
QUESTION:
Implement a function called "predict_subscription_plan" that takes four non-negative integer parameters: the number of shirts, hats, jeans, and shoes a customer has purchased. The function should return the predicted subscription plan ("Basic", "Premium", or "Ultimate") based on the following rules:
- If the customer has purchased more than 200 shirts, more than 100 hats, more than 500 jeans, or more than 300 shoes, they are eligible for the Ultimate plan.
- If the customer has purchased more than 100 shirts, more than 50 hats, or more than 400 hats, they are eligible for the Premium plan if they are not eligible for the Ultimate plan.
- Otherwise, the customer is eligible for the Basic plan.
"""

def predict_subscription_plan(shirts, hats, jeans, shoes):
    if shirts > 200 or hats > 100 or jeans > 500 or shoes > 300:
        return "Ultimate"
    elif shirts > 100 or hats > 50 or jeans > 400 or shoes > 300:
        return "Premium"
    else:
        return "Basic"