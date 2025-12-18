"""
QUESTION:
Write a function `categorize_growth_rates` that takes a list of integers `population_growth` as input and returns a tuple of three lists: positive_growth, negative_growth, and zero_growth. The positive_growth list should contain all the positive growth rates, the negative_growth list should contain all the negative growth rates, and the zero_growth list should contain all the zero growth rates. The input list will only contain integers.
"""

def categorize_growth_rates(population_growth):
    positive_growth = [rate for rate in population_growth if rate > 0]
    negative_growth = [rate for rate in population_growth if rate < 0]
    zero_growth = [rate for rate in population_growth if rate == 0]
    return (positive_growth, negative_growth, zero_growth)