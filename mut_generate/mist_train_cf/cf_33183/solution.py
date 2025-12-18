"""
QUESTION:
Implement a function `calculate_cart_total` that takes in a list of dictionaries representing cart items, where each dictionary contains the item's name and price, and returns a dictionary containing the total cost, item count, and the list of cart items. The function should calculate the total cost by summing the prices of all items and the item count by counting the number of items. The returned dictionary should have keys 'cart_items', 'total', and 'item_count'. The input list of cart items is not empty and each dictionary in the list has keys 'item' and 'price'.
"""

from typing import List, Dict, Union

def calculate_cart_total(cart_items: List[Dict[str, Union[str, float]]]) -> Dict[str, Union[float, int, List[Dict[str, Union[str, float]]]]]:
    total = 0.0
    item_count = len(cart_items)

    for item in cart_items:
        total += item['price']

    return {
        'cart_items': cart_items,
        'total': total,
        'item_count': item_count,
    }