"""
QUESTION:
Create a data structure to store information for items in an online grocery store. The data should include the name of each item, the quantity available, the price per unit, and the nutritional information (calories, carbohydrates, and vitamins).
"""

def create_grocery_item(name, quantity, price, calories, carbohydrates, vitamins):
    """
    Creates a data structure for an item in the grocery store.
    
    Args:
    name (str): The name of the item.
    quantity (int): The quantity available of the item.
    price (float): The price per unit of the item.
    calories (int): The calories in the item.
    carbohydrates (int): The carbohydrates in the item.
    vitamins (list): The vitamins in the item.
    
    Returns:
    dict: A dictionary containing the item's information.
    """
    return {
        "name": name,
        "quantity": quantity,
        "price": price,
        "nutritional_info": {
            "calories": calories,
            "carbohydrates": carbohydrates,
            "vitamins": vitamins
        }
    }