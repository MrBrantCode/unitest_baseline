"""
QUESTION:
Create a function named `Car` that takes in a `base_price` and optional parameters `optional_features` and `taxes`. The function should calculate the total price of a car based on the `base_price`, `optional_features`, and `taxes`. The `base_price` is required, while `optional_features` and `taxes` are optional and default to an empty list and 0, respectively. The `optional_features` should be a list of dictionaries, where each dictionary contains 'name' and 'price' keys. The `taxes` should be a decimal value representing the tax rate. The function should return the total price of the car, which includes the `base_price`, the sum of the prices of `optional_features`, and the tax amount calculated as a percentage of the total price before taxes.
"""

def Car(base_price, optional_features=None, taxes=None):
    """
    Calculate the total price of a car based on its base price, optional features, and taxes.

    Args:
    base_price (float): The base price of the car.
    optional_features (list, optional): A list of dictionaries containing 'name' and 'price' keys. Defaults to None.
    taxes (float, optional): A decimal value representing the tax rate. Defaults to None.

    Returns:
    float: The total price of the car.
    """
    total_price = base_price
    if optional_features:
        for feature in optional_features:
            total_price += feature['price']
    if taxes is not None:
        total_price += total_price * taxes
    return total_price