"""
QUESTION:
Implement a function `vending_machine(item: Literal['cola', 'chips', 'candy'], money_inserted: float) -> str` that simulates a vending machine with items 'cola' ($1.5), 'chips' ($1.0), and 'candy' ($1.75). The function should return a string response based on the following rules: 
- If the item is available and the user has inserted enough money, return "Item Dispensed: <item_name>".
- If the item is available but the user has not inserted enough money, return "Insufficient funds. Please insert <amount_needed> more." where <amount_needed> is the additional amount required to purchase the item.
- If the item is not available, return "Item unavailable. Please make another selection."
"""

def vending_machine(item: str, money_inserted: float) -> str:
    items = {'cola': 1.5, 'chips': 1.0, 'candy': 1.75}
    
    if item in items:
        price = items[item]
        if money_inserted >= price:
            return f"Item Dispensed: {item}"
        else:
            return f"Insufficient funds. Please insert {price - money_inserted} more."
    else:
        return "Item unavailable. Please make another selection."