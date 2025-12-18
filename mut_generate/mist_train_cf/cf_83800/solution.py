"""
QUESTION:
Create a function `cumulative_total` that takes a list of numbers (which can be positive, negative, or decimal up to 2 decimal places) as input and returns a list of cumulative totals, rounded to 2 decimal places. The function should be able to handle lists with varying lengths and values.
"""

def cumulative_total(lst):
    total = 0
    cumulative_total_list = []
    for num in lst:
        total += num
        cumulative_total_list.append(round(total, 2))
    return cumulative_total_list