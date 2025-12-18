"""
QUESTION:
Write a function `min_stamps` that takes a list of distinct philatelic stamp denominations and a specific total postal value as input, and returns the least number of stamps required to reach the total postal value. The function should assume an unlimited number of each type of stamp is available and only works if the problem has a possible solution.
"""

def min_stamps(stamps, total_value):
    """
    Calculate the least number of stamps required to reach the total postal value.

    Args:
    stamps (list): A list of distinct philatelic stamp denominations.
    total_value (int): The specific total postal value.

    Returns:
    int: The least number of stamps required to reach the total postal value.
    """

    # Create a list of length total_value + 1, initialized with a large value (like Infinity) except for the 0th position, which is initialized with 0.
    min_stamps = [float('inf')] * (total_value + 1)
    min_stamps[0] = 0

    # Iterate from the smallest to the largest postal value.
    for i in range(1, total_value + 1):
        # For each value i, iterate through each stamp denomination j.
        for j in stamps:
            # If j is less than or equal i, update min_stamps[i] = min(min_stamps[i], min_stamps[i - j] + 1).
            if j <= i:
                min_stamps[i] = min(min_stamps[i], min_stamps[i - j] + 1)

    # Return min_stamps[total_value] which will contain the least number of stamps required to reach the specific total postal value.
    return min_stamps[total_value]