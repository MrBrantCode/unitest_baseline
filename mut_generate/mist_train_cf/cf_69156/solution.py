"""
QUESTION:
Develop a function called `calculate_total_cost` that calculates the total cost of items in a shopping cart. The function should accept a list of dictionaries where each dictionary represents an item in the shopping cart. Each item dictionary should contain the keys "item", "category", and either "price_per_item" (for electronics), "price_per_page" and "pages" (for books), or "price_per_kg" and "weight" (for fruits and vegetables). The function should return the total cost of all items in the cart. If an item is missing a required price or does not belong to a recognized category (electronics, books, or fruits and vegetables), the function should return an error message.
"""

def calculate_total_cost(shopping_cart):
    total_cost = 0
    for item in shopping_cart:
        if item["category"] == "electronics":
            if "price_per_item" in item:
                total_cost += item["price_per_item"]
            else:
                return f"The item {item['item']} does not have a designated price."
        elif item["category"] == "books":
            if "price_per_page" in item and "pages" in item:
                total_cost += item["price_per_page"] * item["pages"]
            else:
                return f"The item {item['item']} does not have a designated price."
        elif item["category"] == "fruits_vegetables":
            if "price_per_kg" in item and "weight" in item:
                total_cost += item["price_per_kg"] * item["weight"]
            else:
                return f"The item {item['item']} does not have a designated price."
        else:
            return f"The item {item['item']} does not belong to any designated category."
    return total_cost