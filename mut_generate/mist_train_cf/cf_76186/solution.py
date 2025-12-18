"""
QUESTION:
Calculate the extraction amounts from two iron ore deposits with different yields. 

Function name: calculate_extraction_amounts 

Information: Given a total investment of $1000 and a net yield of $55, with a 5% yield from the first deposit and a 7% yield from the second deposit, determine the extraction amount from both deposits.

Restrictions: Assume the investment in the first deposit is x and the investment in the second deposit is 1000 - x.
"""

def calculate_extraction_amounts(total_investment, total_yield, yield1, yield2):
    """
    Calculate the extraction amounts from two iron ore deposits with different yields.

    Args:
        total_investment (float): The total investment.
        total_yield (float): The total yield.
        yield1 (float): The yield from the first deposit.
        yield2 (float): The yield from the second deposit.

    Returns:
        tuple: The extraction amounts from the first and second deposits.
    """
    investment1 = (total_yield - (total_investment * yield2)) / (yield1 - yield2)
    investment2 = total_investment - investment1
    extraction1 = investment1 * yield1
    extraction2 = investment2 * yield2
    return extraction1, extraction2