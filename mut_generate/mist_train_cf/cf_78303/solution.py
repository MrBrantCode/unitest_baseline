"""
QUESTION:
Write a function `calculate_investments(total_investment)` that takes the total investment amount as input and calculates the individual investments of the technology, financial, and marketing partners, as well as the investment amount of each other investor and the number of such investors. The technology partner invests 30% more than the financial partner, the marketing partner invests 20% less than the financial partner, and the remaining investment amount is divided equally among the other investors.
"""

def calculate_investments(total_investment):
    """
    Calculate the individual investments of the technology, financial, and marketing partners,
    as well as the investment amount of each other investor and the number of such investors.

    Parameters:
    total_investment (float): The total investment amount.

    Returns:
    dict: A dictionary containing the investment amounts of each partner and the other investors.
    """

    # The financial partner's investment
    f = total_investment / (1 + 1.3 + 0.8 + 1)
    t = f + 0.3 * f
    m = f - 0.2 * f
    o = total_investment - f - t - m

    # Each other investor, there are 10 such investors 
    x = o / 10

    return {
        "Technology Partner": round(t, 2),
        "Financial Partner": round(f, 2),
        "Marketing Partner": round(m, 2),
        "Other investors": round(x, 2)
    }