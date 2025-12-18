"""
QUESTION:
You are given a list of trees where each tree produces fruit with a certain type, represented by a number. You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each. However, you can only carry a maximum of 5 fruits of each type. 

Write a function `total_fruits(tree)` where `tree` is the list of fruit types. The function should return the total amount of fruit you can collect and the types of fruits collected in each basket. The function should iterate over the list of trees only once, and the space complexity should be O(1) (i.e., the space used does not grow with the size of the input).
"""

from collections import defaultdict

def total_fruits(tree):
    basket = defaultdict(int)
    i = res = 0
    for j, v in enumerate(tree):
        basket[v] += 1
        while len(basket) > 2 or (len(basket) == 2 and max(basket.values()) > 5):
            basket[tree[i]] -= 1
            if basket[tree[i]] == 0:
                del basket[tree[i]]
            i += 1
        res = max(res, j - i + 1)
    return res, list(basket.keys())