"""
QUESTION:
Write a function `optimal_distribution` that takes two parameters: `total`, the total amount of beverages to be served, and `drink_volumes`, a list of volumes for each type of drink (in the order of coffee and other drinks). 

Assuming the amount of coffee served is double the amount of every individual drink and all types of drinks are served, calculate the optimal distribution of containers, bottles, and cans needed for each drink, minimizing the total number of containers, bottles, and cans. 

The function should return a list of the number of containers, bottles, or cans needed for each drink. 

The input list `drink_volumes` has at least two elements, with the first element representing the volume of coffee.
"""

def optimal_distribution(total, drink_volumes):
    # first compute the total volume for each type of drink
    drink_total_vol = [total / (2 + len(drink_volumes) - 1)] * len(drink_volumes)
    drink_total_vol[0] *= 2

    # then compute how many containers, bottles, or cans we need for each
    # making sure to round up because we can't have partial containers
    drink_counts = [int(-(-v // drink_volumes[i])) for i,v in enumerate(drink_total_vol)]

    return drink_counts