"""
QUESTION:
Implement the `calculate_eoq` method in the `InventoryManager` class, which takes in `demand_rate` and uses the Economic Production Quantity (EPQ) model to calculate the Economic Order Quantity (EOQ). The EPQ model formula is EOQ = sqrt((2 * D * S) / H), where D is the demand rate, S is the ordering cost per order, and H is the holding cost per unit per year. The method should return the calculated EOQ value. The class `InventoryManager` has two instance variables: `holding_cost` and `reorder_cost`, representing the holding cost per unit and the cost of placing an order, respectively.
"""

def calculate_eoq(demand_rate, reorder_cost, holding_cost):
    # Calculate EOQ using EPQ model formula
    eoq = ((2 * demand_rate * reorder_cost) / holding_cost) ** 0.5
    return eoq