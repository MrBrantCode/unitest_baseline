"""
QUESTION:
Create a function named calculate_expected_ranks that takes a dictionary of stock data and a dictionary of groups. The stock data dictionary should have stock names as keys and a dictionary with a 'close' key containing a list of closing prices as values. The groups dictionary should have stock names as keys and group values as values. The function should return a dictionary where the keys are the stock names and the values are lists of the expected ranks of the closing prices for each stock. The expected rank is calculated by ranking the closing prices within each group and then dividing by the total number of values in the group.
"""

import pandas as pd

def calculate_expected_ranks(data: dict, groups: dict) -> dict:
    expected_ranks = {}
    for stock, stock_data in data.items():
        closing_prices = stock_data['close']
        group_value = groups[stock]
        df = pd.DataFrame(closing_prices, columns=['close'])
        df['group'] = group_value
        rank_values = df.groupby('group')['close'].rank(method='min') / df['group'].value_counts().loc[group_value]
        expected_ranks[stock] = list(rank_values)
    return expected_ranks