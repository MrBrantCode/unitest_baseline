"""
QUESTION:
Create a `Car` class with a method `calculate_total_price` that takes the base price, optional features, and taxes into account to calculate the total price of the car. The `Car` class should have the following properties: 

- `base_price`: a required argument when creating a `Car` object.
- `optional_features`: an optional argument with a default value that should be a list of dictionaries, where each dictionary contains the name and price of an optional feature.
- `taxes`: an optional argument with a default value representing the tax rate.

The `calculate_total_price` method should return the sum of the `base_price`, the total price of `optional_features`, and the total tax amount.
"""

def calculate_car_total_price(base_price, optional_features=None, taxes=None):
    """
    Calculates the total price of a car.

    Args:
        base_price (float): The base price of the car.
        optional_features (list, optional): A list of dictionaries, where each dictionary contains the name and price of an optional feature. Defaults to None.
        taxes (float, optional): The tax rate. Defaults to None.

    Returns:
        float: The total price of the car.
    """
    
    total_price = base_price
    if optional_features is not None:
        for feature in optional_features:
            total_price += feature['price']
    if taxes is not None:
        total_price += total_price * taxes
    return total_price