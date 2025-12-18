"""
QUESTION:
Write a function `prob_same_color` that takes the total number of marbles and the number of marbles of the same color as input, and returns the probability of drawing two marbles of the same color consecutively without replacement. The function should calculate the probability as (number of marbles of the same color / total number of marbles) * ((number of marbles of the same color - 1) / (total number of marbles - 1)). Use this function to find the total probability that either both marbles are red, both are blue, both are green, or both are yellow, given 4 red marbles, 6 blue marbles, 3 green marbles, 5 yellow marbles, and a total of 18 marbles.
"""

def prob_same_color(total_marbles, same_color_marbles):
    return (same_color_marbles / total_marbles) * ((same_color_marbles - 1) / (total_marbles - 1))