"""
QUESTION:
You can print your name on a billboard ad. Find out how much it will cost you. Each letter has a default price of £30, but that can be different if you are given 2 parameters instead of 1.

You can not use multiplier "*" operator.

If your name would be Jeong-Ho Aristotelis, ad would cost £600.
20 leters * 30 = 600 (Space counts as a letter).
"""

def calculate_billboard_cost(name: str, price_per_letter: int = 30) -> int:
    """
    Calculate the total cost to print a name on a billboard.

    :param name: The name to be printed on the billboard.
    :param price_per_letter: The cost per letter. Default is 30.
    :return: The total cost to print the name.
    """
    return sum((price_per_letter for letter in name))