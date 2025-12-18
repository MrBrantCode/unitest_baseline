"""
QUESTION:
Create a function named `calculate_total` that takes in the user's name (`user`), a list of item names (`items_list`), and an optional discount code (`discount_code`). The function should calculate the total cost of the items in the list with the discount applied if a discount code is provided. The function should also store the purchase history for the user, including the items purchased and the total cost. The function should use the `items` dictionary to get the price of each item and the `discounts` dictionary to get the discount percentage for the discount code. The purchase history should be stored in a dictionary called `users`.
"""

items = {
    "item1": 10,
    "item2": 20,
    "item3": 30
}
discounts = {
    "CODE1": 10,
    "CODE2": 20,
    "CODE3": 30
}
users = {}

def calculate_total(user, items_list, discount_code=None):
    """
    Calculate the total cost of the items in the list with the discount applied if a discount code is provided.
    
    Args:
        user (str): The user's name.
        items_list (list): A list of item names.
        discount_code (str, optional): The discount code. Defaults to None.
    
    Returns:
        float: The total cost of the items.
    """
    total = 0
    for item in items_list:
        total += items[item]
    if discount_code:
        total *= (100 - discounts[discount_code])/100
    if user not in users:
        users[user] = {"purchase_history": []}
    users[user]["purchase_history"].append((items_list, total))
    return total