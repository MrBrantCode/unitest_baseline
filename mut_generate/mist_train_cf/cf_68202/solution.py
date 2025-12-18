"""
QUESTION:
Create a function `num_ways_to_tile(n)` that calculates the total number of ways to tile a linear stretch measuring `n` units in length using grey square tiles, crimson tiles (length of two units), emerald tiles (length of three units), and azure tiles (length of four units). The function should take an integer `n` as input and return the total number of ways to tile the linear stretch.
"""

def num_ways_to_tile(n):
    """
    Calculate the total number of ways to tile a linear stretch measuring n units in length.
    
    Args:
    n (int): The length of the linear stretch.

    Returns:
    int: The total number of ways to tile the linear stretch.
    """
    ways = [0]*(n+1)
    ways[0] = 1
    for i in range(1, len(ways)):
        ways[i] += ways[i-1]
        if i-2 >= 0:
            ways[i] += ways[i-2]
        if i-3 >= 0:
            ways[i] += ways[i-3]
        if i-4 >= 0:
            ways[i] += ways[i-4]
    return ways[-1]