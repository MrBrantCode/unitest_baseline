"""
QUESTION:
Create a function called `format_discounted_price` that takes two arguments: `original_price` and `discount`. The function should return a formatted string that includes the original price rounded to two decimal places, the discount as a 2-digit percentage value, and the discounted price rounded to two decimal places with a dollar sign and comma as thousand separators. The discounted price should also be displayed in red font color.
"""

def format_discounted_price(original_price, discount):
    """
    Format a string for a discounted price.

    Args:
        original_price (float): The original price of the item.
        discount (float): The discount percentage.

    Returns:
        str: A formatted string that includes the original price, discount, and discounted price.
    """
    rounded_original_price = "{:.2f}".format(original_price)
    discounted_price = original_price * (1 - discount/100)
    rounded_discounted_price = "{:.2f}".format(discounted_price)
    formatted_discounted_price = "${:,.2f}".format(discounted_price)
    formatted_discount = "{:.0f}%".format(discount)
    formatted_discounted_price_red = "\033[31m" + formatted_discounted_price + "\033[0m"

    return f"Original Price: ${rounded_original_price}\nDiscount: {formatted_discount}\nDiscounted Price: {formatted_discounted_price_red}"