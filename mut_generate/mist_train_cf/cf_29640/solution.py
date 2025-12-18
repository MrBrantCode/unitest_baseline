"""
QUESTION:
Implement the function `calculate_total_cost(cart, discount_rules)` to calculate the total cost of a shopping cart after applying discounts. The function takes two parameters: `cart`, a list of dictionaries representing items with keys "name", "price", and "quantity", and `discount_rules`, a list of dictionaries with keys "item", "quantity", and "discount" representing the discount rules. Apply the discounts to the corresponding items in the cart and return the total cost.
"""

def calculate_total_cost(cart, discount_rules):
    total_cost = 0
    item_quantities = {item["name"]: item["quantity"] for item in cart}
    
    for item in cart:
        item_cost = item["price"] * item["quantity"]
        if item["name"] in [rule["item"] for rule in discount_rules]:
            discount_rule = next((rule for rule in discount_rules if rule["item"] == item["name"]), None)
            if item["quantity"] >= discount_rule["quantity"]:
                item_cost -= (item_cost * discount_rule["discount"] / 100)
        total_cost += item_cost
    
    return total_cost