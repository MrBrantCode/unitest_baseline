"""
QUESTION:
Calculate the average GDP growth rate and average inflation rate for a given period. 

Create a function named `calculate_cagr` that takes a dictionary of economic data as input, where each key is a year and each value is another dictionary containing the GDP and inflation rate for that year. The function should return the compounded annual growth rate (CAGR) for GDP and inflation. 

The CAGR should be calculated using the formula: CAGR = (Ending Value / Beginning Value) ^ (1 / Number of Years) - 1. For inflation rates, the formula is: CAGR = ((1 + Ending Value) / (1 + Beginning Value)) ^ (1 / Number of Years) - 1.

Restrictions: The input dictionary should contain at least two years of data, and the GDP and inflation rates should be provided as numbers.
"""

def calculate_cagr(economic_data):
    """
    Calculate the compounded annual growth rate (CAGR) for GDP and inflation.

    Args:
        economic_data (dict): A dictionary of economic data where each key is a year
                              and each value is another dictionary containing the GDP
                              and inflation rate for that year.

    Returns:
        tuple: A tuple containing the CAGR for GDP and inflation.
    """
    start_year = min(economic_data.keys())
    end_year = max(economic_data.keys())
    years = end_year - start_year

    gdp_start = economic_data[start_year]["gdp"]
    gdp_end = economic_data[end_year]["gdp"]
    inflation_start = economic_data[start_year]["inflation"]
    inflation_end = economic_data[end_year]["inflation"]

    gdp_cagr = ((gdp_end / gdp_start) ** (1 / years)) - 1
    inflation_cagr = ((1 + inflation_end) / (1 + inflation_start)) ** (1 / years) - 1

    return gdp_cagr, inflation_cagr