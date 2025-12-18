"""
QUESTION:
Write a function `calculate_gdp_inflation_rates` that takes a dictionary of economic data as input, where each key is a year and each value is another dictionary containing the GDP and inflation rate for that year. The function should calculate and return the compounded annual growth rate (CAGR) for both GDP and inflation over the given period. The input dictionary is guaranteed to have at least two entries. The CAGR should be calculated using the formula: CAGR = (Ending Value / Beginning Value) ^ (1 / Number of Years) - 1. For inflation, the formula should be adjusted to: CAGR = ((1 + Ending Value) / (1 + Beginning Value)) ^ (1 / Number of Years) - 1. The function should return the results as a tuple of two values: the average GDP growth rate and the average inflation rate.
"""

def calculate_gdp_inflation_rates(data):
    years = sorted(data.keys())
    gdp_cagr = (data[years[-1]]["gdp"] / data[years[0]]["gdp"]) ** (1/len(years)) - 1
    inflation_cagr = ((1 + data[years[-1]]["inflation"]) / (1 + data[years[0]]["inflation"])) ** (1/len(years)) - 1
    return gdp_cagr, inflation_cagr