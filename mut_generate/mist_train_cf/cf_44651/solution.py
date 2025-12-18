"""
QUESTION:
Write a function called `pagoda_cubes` that calculates the total number of cubes required to construct a pagoda with a specified number of tiers. Each tier of the pagoda has a square base with a side length 2 units less than the tier below it. The function should take one integer argument, `tiers`, which represents the number of tiers in the pagoda.
"""

def pagoda_cubes(tiers):
    """
    Calculate the total number of cubes required to construct a pagoda with a specified number of tiers.
    
    Args:
        tiers (int): The number of tiers in the pagoda.
    
    Returns:
        int: The total number of cubes required.
    """
    total_cubes = 0
    for i in range(tiers, 0, -1):
        tier_size = 2 * i - 1
        if tier_size > 0:
            total_cubes += tier_size ** 2
    return total_cubes