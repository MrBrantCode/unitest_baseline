"""
QUESTION:
Create a function called `format_discounted_price` that takes two parameters: `original_price` and `discount`. The function should return a formatted string displaying the original price rounded to two decimal places, the discount as a 2-digit percentage, and the discounted price rounded to two decimal places, displayed with a dollar sign, thousand separators, and in red font color.
"""

def format_discounted_price(original_price, discount):
    """
    Formats a string displaying the original price, discount, and discounted price.

    Args:
        original_price (float): The original price of an item.
        discount (float): The discount percentage.

    Returns:
        str: A formatted string displaying the original price, discount, and discounted price.
    """

    # Calculate the discounted price
    discounted_price = original_price * (1 - discount/100)

    # Format the original price, discount, and discounted price
    rounded_original_price = "{:.2f}".format(original_price)
    formatted_discount = "{:.0f}%".format(discount)
    formatted_discounted_price = "${:,.2f}".format(discounted_price)

    # Display the discounted price in red font color
    formatted_discounted_price_red = "\033[31m" + formatted_discounted_price + "\033[0m"

    # Create the formatted string
    formatted_string = f"Original Price: ${rounded_original_price}\nDiscount: {formatted_discount}\nDiscounted Price: {formatted_discounted_price_red}"

    return formatted_string