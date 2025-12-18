"""
QUESTION:
Write a function `calculate_total_cost` that takes in two parameters: `sizes` and `desired`. `sizes` is a list of integers representing available sizes in a store, and `desired` is a list of tuples where each tuple contains an integer size and an integer price. Return the total amount of money required to purchase all desired items, considering each size can only be used once.
"""

from collections import Counter

def calculate_total_cost(sizes, desired):
    count = Counter(sizes)
    money = 0
    for dlist in desired:
        if dlist[0] in sizes:
            if count[dlist[0]] != 0:
                count[dlist[0]] -= 1
                money += dlist[1]
    return money