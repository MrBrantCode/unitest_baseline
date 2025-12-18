"""
QUESTION:
Implement the `combine_coindata(coindata_cmb)` function to combine coin data from a list of dictionaries into a single dictionary. The input `coindata_cmb` is a dictionary containing a list of dictionaries, where each inner dictionary represents a coin's attributes and values. The function should return a dictionary where keys are coin attributes and values are lists of attribute values for each coin, with None for missing attributes.
"""

import collections

def combine_coindata(coindata_cmb):
    combined_coindata = collections.defaultdict(list)
    for coin_data in coindata_cmb["data"]:
        for attribute, value in coin_data.items():
            combined_coindata[attribute].append(value)
    return dict(combined_coindata)