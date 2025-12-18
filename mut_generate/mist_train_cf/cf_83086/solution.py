"""
QUESTION:
otalFruit(tree): In a linear orchard where the i-th tree yields a fruit of type tree[i], you can start at any tree and continuously harvest a fruit from the current tree and move to the tree to the right, with the goal of filling two baskets with each containing only one type of fruit. Return the maximum quantity of fruit you can harvest. The input tree is a list of integers where 1 <= tree.length <= 40000 and 0 <= tree[i] < tree.length.
"""

from collections import defaultdict

def totalFruit(tree):
    """
    Returns the maximum quantity of fruit that can be harvested in a linear orchard.
    
    Args:
    tree (list): A list of integers where 1 <= tree.length <= 40000 and 0 <= tree[i] < tree.length.

    Returns:
    int: The maximum quantity of fruit that can be harvested.
    """
    fruit_count = defaultdict(int)
    max_harvest = 0
    left = 0

    for right, fruit in enumerate(tree):
        fruit_count[fruit] += 1

        while len(fruit_count) > 2:
            fruit_count[tree[left]] -= 1
            if fruit_count[tree[left]] == 0:
                del fruit_count[tree[left]]
            left += 1

        max_harvest = max(max_harvest, right - left + 1)

    return max_harvest