"""
QUESTION:
Create a function named `high_profit_orders` that takes a list of orders as input, where each order is a dictionary containing customer information and a list of products. Each product is a dictionary with keys 'name', 'cost', and 'price'. The function should calculate the profit margin for each product, which is defined as the difference between the selling price and the production cost, divided by the selling price. It should return a list of orders that contain products with a profit margin greater than 50%, including the customer name, address, and total order cost.
"""

def high_profit_orders(orders):
    high_profit_products = []
    high_profit_orders = []

    for order in orders:
        for product in order["products"]:
            profit_margin = (product["price"] - product["cost"]) / product["price"]
            if profit_margin > 0.5:
                high_profit_products.append(product)
                if order not in high_profit_orders:
                    high_profit_orders.append(order)

    result = []
    for order in high_profit_orders:
        total_cost = sum(p["price"] for p in order["products"])
        result.append({
            "customer": order["customer"],
            "address": order["address"],
            "total_cost": total_cost
        })

    return result