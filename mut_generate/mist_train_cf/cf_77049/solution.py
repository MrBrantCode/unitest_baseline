"""
QUESTION:
Determine the quantities of two types of fertilizers, one with 5lbs of nitrogen per unit and the other with 7lbs of nitrogen per unit, required to achieve a total of 36lbs of nitrogen. The function should be named `fertilizer_combination`.
"""

def fertilizer_combination(nitrogen_content):
    """
    Determine the quantities of two types of fertilizers, one with 5lbs of nitrogen per unit 
    and the other with 7lbs of nitrogen per unit, required to achieve a total of 'nitrogen_content' lbs of nitrogen.

    Args:
        nitrogen_content (int): The total nitrogen content required.

    Returns:
        tuple: A tuple containing the number of 5lb and 7lb fertilizer bags required.
    """
    for five_bags in range(nitrogen_content // 5 + 1):
        seven_bags = (nitrogen_content - five_bags * 5) / 7
        if seven_bags.is_integer() and seven_bags >= 0:
            return five_bags, int(seven_bags)
    return None