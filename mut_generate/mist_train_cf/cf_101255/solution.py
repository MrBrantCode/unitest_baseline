"""
QUESTION:
Create a function `analyze_orders` that takes a list of orders as input. Each order is a dictionary containing customer information and a list of products. Each product is a dictionary with keys 'name', 'cost', and 'price'. Calculate the profit margin for each product and return a list of orders that contain products with a profit margin greater than 50%. The returned orders should include customer name, address, and total order cost.
"""

def analyze_orders(orders):
    high_profit_orders = []
    for order in orders:
        total_cost = sum(product["price"] for product in order["products"])
        for product in order["products"]:
            profit_margin = (product["price"] - product["cost"]) / product["price"]
            if profit_margin > 0.5:
                high_profit_orders.append({
                    "customer": order["customer"],
                    "address": order["address"],
                    "total_cost": total_cost
                })
                break
    return high_profit_orders