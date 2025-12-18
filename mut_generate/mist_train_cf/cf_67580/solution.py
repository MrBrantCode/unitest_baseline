"""
QUESTION:
You are given a function `min_stamps` with two parameters: a list of distinct postage stamp denominations `stamps` and a target total postage cost `total_cost`. Your task is to determine the least number of stamps required to reach `total_cost` using the given `stamps`. The function should return the minimum number of stamps required. If no combination of stamps can sum up to `total_cost`, the function should return a value indicating that a solution is not possible, such as `float('inf')`. The function should assume that there is an infinite supply of each kind of stamp.
"""

def min_stamps(stamps, total_cost):
    """
    This function determines the least number of stamps required to reach a target total postage cost using the given stamps.

    Args:
    stamps (list): A list of distinct postage stamp denominations.
    total_cost (int): The target total postage cost.

    Returns:
    int: The minimum number of stamps required. If no combination of stamps can sum up to total_cost, it returns float('inf').
    """
    
    # Initialize a list to store the minimum number of stamps required for each total cost from 0 to total_cost
    min_stamps_required = [float('inf')] * (total_cost + 1)
    
    # We need 0 stamps to make a total cost of 0
    min_stamps_required[0] = 0

    # For each total cost from 1 to total_cost
    for cost in range(1, total_cost + 1):
        # For each stamp denomination
        for stamp in stamps:
            # If the stamp denomination is less than or equal to the current total cost
            if stamp <= cost:
                # If using this stamp results in a smaller number of stamps, update the minimum number of stamps required
                min_stamps_required[cost] = min(min_stamps_required[cost], min_stamps_required[cost - stamp] + 1)

    # Return the minimum number of stamps required to reach the target total cost
    return min_stamps_required[total_cost] if min_stamps_required[total_cost] != float('inf') else -1