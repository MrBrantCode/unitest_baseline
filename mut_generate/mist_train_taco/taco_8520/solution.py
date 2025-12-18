"""
QUESTION:
We need to write some code to return the original price of a product, the return type must be of type decimal and the number must be rounded to two decimal places.

We will be given the sale price (discounted price), and the sale percentage, our job is to figure out the original price.


### For example:

Given an item at $75 sale price after applying a 25% discount, the function should return the original price of that item before applying the sale percentage, which is ($100.00) of course, rounded to two decimal places.


DiscoverOriginalPrice(75, 25) => 100.00M where 75 is the sale price (discounted price), 25 is the sale percentage and 100 is the original price
"""

def calculate_original_price(discounted_price: float, sale_percentage: float) -> float:
    """
    Calculate the original price of a product given the discounted price and the sale percentage.

    :param discounted_price: The sale price after applying the discount.
    :param sale_percentage: The percentage of the discount applied to the original price.
    :return: The original price of the product before the discount was applied, rounded to two decimal places.
    """
    original_price = discounted_price / ((100 - sale_percentage) * 0.01)
    return round(original_price, 2)