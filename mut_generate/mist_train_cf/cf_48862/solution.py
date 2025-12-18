"""
QUESTION:
Write a function that uses itertools.groupby() to group a list of dictionaries by a certain key, performs aggregation on the grouped data, and then filters or calculates additional information based on the grouped data. The function should take in a list of dictionaries and a key to group by as input, and return a dictionary with the aggregated and filtered data. The function should also handle cases where the input data is not sorted by the key.
"""

import itertools

def entrance(data, key):
    # Sorting the list of dictionaries based on key
    data.sort(key = lambda i: i[key])

    # Grouping the data using itertools.groupby
    grouped_data = itertools.groupby(data, key=lambda x: x[key])

    # aggregating scores for each group
    aggregated_data = {}
    for k, v in grouped_data:
        items = list(v)
        aggregated_data[k] = {
            'count': len(items),
            'avg': round(sum(i['grade'] for i in items) / len(items), 2)
        }
    return aggregated_data