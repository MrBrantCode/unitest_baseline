"""
QUESTION:
Design a function `fruit_distribution` that calculates the distribution of fruits in a basket given a list of strings representing the count of various fruits, the total number of fruits in the basket, and a list of all possible fruits. The function should return a dictionary containing the count of each fruit that is not specified in the input list or has a non-zero count.

Input:
- A list of strings `s` (1 <= len(s) <= 100) where each string follows the format: "X fruit_name".
- An integer `n` (0 <= n <= 10^6) representing the total number of fruits in the basket.
- A list of strings `fruits` (1 <= len(fruits) <= 1000) where each string is a fruit name.

Output:
- A dictionary containing the count of each fruit that is not specified in the input list `s` or has a non-zero count.
"""

from typing import List, Dict

def fruit_distribution(s: List[str], n: int, fruits: List[str]) -> Dict[str, int]:
    """
    Calculate the distribution of fruits in a basket.

    Args:
    s (List[str]): A list of strings representing the count of various fruits.
    n (int): An integer representing the total number of fruits in the basket.
    fruits (List[str]): A list of strings representing all possible fruits.

    Returns:
    Dict[str, int]: A dictionary containing the count of each fruit that is not specified in the input list s or has a non-zero count.
    """

    # Initialize an empty dictionary to store the count of each fruit
    fruit_count = {}

    # Populate the fruit_count dictionary with fruits and their counts from list s
    for item in s:
        count, fruit = item.split()
        fruit_count[fruit] = int(count)

    # Calculate the total count of fruits specified in list s
    total_count = sum(fruit_count.values())

    # Initialize an empty dictionary to store the distribution of fruits
    distribution = {}

    # Iterate over all possible fruits
    for fruit in fruits:
        # If a fruit is not specified in list s or has a non-zero count, calculate its count
        if fruit not in fruit_count or fruit_count[fruit] == 0:
            distribution[fruit] = max(0, n - total_count)
        else:
            distribution[fruit] = 0

    # Remove fruits with zero count from the distribution dictionary
    distribution = {fruit: count for fruit, count in distribution.items() if count != 0}

    return distribution