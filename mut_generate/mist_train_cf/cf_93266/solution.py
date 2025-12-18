"""
QUESTION:
Create a function called `calculate_total_cost` that takes a list of discounts as input. The function should return the total cost after applying the discounts and the minimum number of items that need to be purchased to achieve the lowest possible cost. The function should handle cases where the discounts list is empty or contains negative values by returning an error message. Do not use any built-in Python functions or libraries for calculating permutations or combinations.
"""

def calculate_total_cost(discounts):
    """
    Calculate the total cost after applying the discounts and the minimum number of items that need to be purchased to achieve the lowest possible cost.

    Args:
    discounts (list): A list of discounts.

    Returns:
    tuple: A tuple containing the total cost and the minimum number of items.
    """
    
    if not discounts or any(d < 0 for d in discounts):
        return "Invalid discounts list"

    min_items = float('inf')
    min_cost = float('inf')

    def combinations(lst, r):
        if r == 0:
            yield []
        elif r > 0 and lst:
            for i in range(len(lst)):
                for comb in combinations(lst[i+1:], r-1):
                    yield [lst[i]] + comb

    for i in range(1, len(discounts) + 1):
        for comb in combinations(discounts, i):
            cost = sum(discounts) - sum(comb)
            items = len(discounts) - i + 1

            if cost < min_cost:
                min_cost = cost
                min_items = items

    return min_cost, min_items