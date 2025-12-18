"""
QUESTION:
Create a function `get_fruit_price` that takes a `fruit_name` and a `customer_age` as input. The function should return the price of the given fruit from a predefined table, applying a 10% discount if the customer is under 18 years old and a 5% discount if the customer is over 65 years old, except for Pineapple. If the fruit is not in the table, return `None`. The fruit prices are as follows: Apple ($0.50), Orange ($0.40), Banana ($0.25), and Pineapple ($1.50).
"""

def get_fruit_price(fruit_name, customer_age):
    # Define the table of fruit prices
    fruit_prices = {
        "Apple": 0.50,
        "Orange": 0.40,
        "Banana": 0.25,
        "Pineapple": 1.50
    }
    # Check if the fruit is in the table
    if fruit_name not in fruit_prices:
        return None
    # Get the base price of the fruit
    base_price = fruit_prices[fruit_name]
    # Apply discounts based on customer age
    if customer_age < 18:
        discount = 0.1
    elif customer_age > 65 and fruit_name != "Pineapple":
        discount = 0.05
    else:
        discount = 0
    # Calculate the final price with discount
    final_price = base_price * (1 - discount)
    return final_price