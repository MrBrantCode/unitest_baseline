"""
QUESTION:
Create a function called `filter_transactions` that takes in a list of transactions and various filter parameters. The function should filter out transactions based on the following conditions: 
- transactions with products purchased within a specified number of days 
- transactions with products exceeding a maximum price limit 
- transactions with products belonging to specific categories 
- transactions with products not in a list of preferred products 
- transactions with products not in a list of preferred categories 
The function should return a list of transactions with customer name, product name, and purchase date for the remaining transactions after applying the filters.
"""

def filter_transactions(transactions, days=60, max_price=500, exclude_categories=None, preferred_products=None, preferred_categories=None):
    filtered_transactions = []
    for transaction in transactions:
        purchase_date = datetime.strptime(transaction["purchase_date"], "%Y-%m-%d")
        days_diff = (datetime.now() - purchase_date).days
        if days_diff <= days:
            continue
        product = transaction["product"]
        if product["price"] > max_price:
            continue
        if exclude_categories and product["category"] in exclude_categories:
            continue
        if preferred_products and product["name"] not in preferred_products:
            continue
        if preferred_categories and product["category"] not in preferred_categories:
            continue
        filtered_transactions.append({
            "customer_name": transaction["customer_name"],
            "product_name": product["name"],
            "purchase_date": transaction["purchase_date"]
        })
    return filtered_transactions