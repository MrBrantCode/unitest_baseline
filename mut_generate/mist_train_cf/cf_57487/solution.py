"""
QUESTION:
Write a function called `calculate_wml` that calculates the winner minus loser (WML) portfolio return. The WML return is the equal-weight average of the returns for the two winner portfolios minus the average of the returns for the two loser portfolios, calculated as 1/2 * (Small Winner + Big Winner) - 1/2 * (Small Loser + Big Loser). The function should take four arguments: `small_winner`, `big_winner`, `small_loser`, and `big_loser`, which are the returns of the corresponding portfolios.
"""

def calculate_wml(small_winner, big_winner, small_loser, big_loser):
    """
    Calculate the winner minus loser (WML) portfolio return.

    The WML return is the equal-weight average of the returns for the two winner portfolios 
    minus the average of the returns for the two loser portfolios.

    Parameters:
    small_winner (float): Return of the small winner portfolio.
    big_winner (float): Return of the big winner portfolio.
    small_loser (float): Return of the small loser portfolio.
    big_loser (float): Return of the big loser portfolio.

    Returns:
    float: The WML portfolio return.
    """
    return 0.5 * (small_winner + big_winner) - 0.5 * (small_loser + big_loser)