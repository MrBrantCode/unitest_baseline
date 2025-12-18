"""
QUESTION:
Write a function called `roses_per_vase` that calculates the total number of roses in each vase after selling a certain number of roses and receiving a new shipment. The function should take four parameters: `initial_roses`, `roses_sold`, `vases`, and `new_shipment`. It should return the total number of roses in each vase after the sale and the addition of the new shipment. Assume the remaining roses and the new shipment are evenly distributed among the vases.
"""

def roses_per_vase(initial_roses, roses_sold, vases, new_shipment):
    """
    Calculate the total number of roses in each vase after selling a certain number of roses and receiving a new shipment.

    Args:
        initial_roses (int): The initial number of roses.
        roses_sold (int): The number of roses sold.
        vases (int): The number of vases.
        new_shipment (int): The number of roses in the new shipment.

    Returns:
        float: The total number of roses in each vase after the sale and the addition of the new shipment.
    """
    return (initial_roses - roses_sold) / vases + new_shipment / vases