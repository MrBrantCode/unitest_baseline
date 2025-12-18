"""
QUESTION:
Create a function called `calculate_new_shares` to determine the amount of shares to allocate to a user when they deposit assets into a mutual fund. The function should take two parameters: the initial_assets, a dictionary representing the initial composition of the mutual fund (e.g., {"A": 1, "B": 1}), and deposited_assets, a dictionary representing the assets deposited by the user (e.g., {"A": 2}). The function should return the number of new shares to allocate to the user. Assume that the mutual fund initially has 1 share allocated and the deposited assets are in the same units as the initial assets.
"""

def calculate_new_shares(initial_assets, deposited_assets):
    """
    Calculate the number of new shares to allocate to a user when they deposit assets into a mutual fund.

    Args:
    initial_assets (dict): The initial composition of the mutual fund.
    deposited_assets (dict): The assets deposited by the user.

    Returns:
    float: The number of new shares to allocate to the user.
    """
    # Calculate the total value of the mutual fund after the deposit
    total_assets = {asset: initial_assets.get(asset, 0) + deposited_assets.get(asset, 0) for asset in set(list(initial_assets.keys()) + list(deposited_assets.keys()))}
    
    # Calculate the increase in assets
    increase_assets = {asset: deposited_assets.get(asset, 0) for asset in deposited_assets}
    
    # Calculate the proportion of the increase in assets to the total assets
    proportion = sum(increase_assets.values()) / sum(total_assets.values())
    
    # Calculate the number of new shares to allocate
    new_shares = proportion
    
    return new_shares