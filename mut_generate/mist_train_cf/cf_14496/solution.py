"""
QUESTION:
Create a function named `calculate_total_cost` that takes a list of discounts as input. The function should calculate the total cost after applying a subset of the discounts and return the minimum total cost along with the minimum number of items needed to achieve that cost. The function should handle cases where the input list is empty or contains negative values, and return an error message in such cases. The function should not use any built-in Python functions or libraries for calculating permutations or combinations.
"""

def calculate_total_cost(discounts):
    if not discounts or any(d < 0 for d in discounts):
        return "Invalid discounts list"

    def combinations(lst, r):
        if r == 0:
            yield []
        elif r > 0 and lst:
            for i in range(len(lst)):
                for comb in combinations(lst[i+1:], r-1):
                    yield [lst[i]] + comb

    min_items = float('inf')
    min_cost = float('inf')

    for i in range(1, len(discounts) + 1):
        for comb in combinations(discounts, i):
            cost = sum(discounts) - sum(comb)
            items = len(discounts) - i + 1

            if cost < min_cost:
                min_cost = cost
                min_items = items

    return min_cost, min_items