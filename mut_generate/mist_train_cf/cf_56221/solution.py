"""
QUESTION:
Develop a function `knapSack` that solves the fractional Knapsack problem using the greedy algorithm, where the goal is to maximize the total value within a given weight constraint `W`. The function should take four parameters: `W` (the weight limit), `wt` (a list of weights for each item), `val` (a list of values corresponding to each item), and `n` (the number of items). The function should return the maximum total value that can be achieved. Note that items can be divided into smaller parts to fill the remaining weight in the knapsack.
"""

def knapSack(W, wt, val, n):
    # initialize an array to store the ratio of value/weight
    ratio = []

    # calculate value/weight ratio and store the result along with index
    for i in range(0, len(val)):
        ratio.append((val[i] / wt[i], i))

    # sort the ratio array in descending order
    ratio.sort(reverse=True)

    max_value = 0
    remaining_weight = W

    # loop through each item in the sorted ratio array
    for value, i in ratio:

        # if adding current weight doesn't exceed total capacity, add it
        if wt[i] <= remaining_weight:
            remaining_weight -= wt[i]
            max_value += val[i]
        else:
            # else, if we can't put the whole item, put the fraction that fits
            fraction = remaining_weight / wt[i]
            max_value += val[i] * fraction
            remaining_weight = 0
            break
    
    return max_value