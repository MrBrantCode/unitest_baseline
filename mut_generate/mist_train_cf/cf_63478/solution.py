"""
QUESTION:
Develop a function `dessert_distribution(s, n, desserts, non_dessert_items)` that takes four inputs: 
- `s`, an integer representing the total quantity of items on the table
- `n`, an integer representing the day the items were served
- `desserts`, a list of strings representing the names of desserts
- `non_dessert_items`, a list of strings representing the quantities of various items on the table, with each string in the format "X item_name"

The function should return two dictionaries: one containing the count of each dessert not listed in `non_dessert_items` and the other containing the counts of non-dessert items. If `n` is even, the count of desserts should decrease by 15%. If the total count of items is fewer than `s`, return 'Error'. The returned dictionaries should only include items with a count greater than zero.
"""

def dessert_distribution(s, n, desserts, non_dessert_items):
    """
    This function takes in the total quantity of items, day of serving, list of desserts, 
    and list of non-dessert items. It returns two dictionaries containing the counts of 
    dessert and non-dessert items, adjusting for a 15% decrease in desserts on even days.

    Args:
        s (int): Total quantity of items on the table
        n (int): Day the items were served
        desserts (list): List of strings representing dessert names
        non_dessert_items (list): List of strings representing quantities of items

    Returns:
        tuple: Two dictionaries containing dessert and non-dessert item counts, or 'Error' if total quantity exceeds s
    """

    desserts_dict = {}
    non_desserts_dict = {}

    for item in non_dessert_items:
        name, quantity = item.split()
        quantity = int(quantity)
        if name in desserts:
            if n % 2 == 0:
                quantity = int(quantity * 0.85)
            if quantity > 0:
                desserts_dict[name] = desserts_dict.get(name, 0) + quantity
        else:
            if quantity > 0:
                non_desserts_dict[name] = non_desserts_dict.get(name, 0) + quantity

    total_quantities = sum(desserts_dict.values()) + sum(non_desserts_dict.values())

    if total_quantities > s:
        return 'Error'

    return desserts_dict, non_desserts_dict