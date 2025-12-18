"""
QUESTION:
Calculate the maximum number of cans of pears that can be bought without exceeding the total money saved. Write a function named `calculate_cans` that takes two parameters: `cost_of_three` (the cost of 3 cans of pears) and `total_money_saved` (the total amount of money saved). The function should return the maximum number of cans of pears that can be afforded as an integer, assuming that cans cannot be split.
"""

def calculate_cans(cost_of_three, total_money_saved):
    cost_of_one = cost_of_three / 3
    cans_affordable = total_money_saved / cost_of_one
    return int(cans_affordable)