"""
QUESTION:
Implement the `update_with_trade_update_rest` method in the `InFlightOrder` class, which takes a dictionary `trade_update` containing 'quantity', 'price', and 'state' as input. The method should return a tuple containing the total quantity filled, total cost of the filled quantity, and the last state of the order. Update the `last_state` property of the order based on the trade update and handle various trade states, including 'FILLED'. 

Restrictions: The method should use the `Decimal` class from the `decimal` module for accurate decimal calculations and return the result as a tuple of `Decimal` and string values.
"""

from decimal import Decimal
from typing import Dict, Any, Tuple

def update_with_trade_update_rest(trade_update: Dict[str, Any], last_state: str, 
                                 total_quantity_filled: float = 0, total_cost: float = 0) -> Tuple[Decimal, Decimal, str]:
    quantity = Decimal(trade_update.get('quantity', 0))
    price = Decimal(trade_update.get('price', 0))
    trade_state = trade_update.get('state', '')

    if trade_state == 'FILLED':
        total_quantity_filled = Decimal(total_quantity_filled) + quantity
        total_cost = Decimal(total_cost) + quantity * price

    last_state = trade_state
    return total_quantity_filled, total_cost, last_state