"""
QUESTION:
Create a function `peculiar_sequence` that takes a non-empty list of positive integers `num_series` and returns a list of tuples. Each tuple contains a unique integer from `num_series` that appears fewer than double its value and the index of its first appearance. The returned list is sorted by the index value. If no such integer exists, return an empty list.
"""

def peculiar_sequence(num_series):
    counter = {}
    sequence = []

    for i, v in enumerate(num_series):
        if v not in counter:
            counter[v] = {'index': i, 'count': 0}
        counter[v]['count'] += 1
    
    for k, v in counter.items():
        if v['count'] < 2*k:
            sequence.append((k, v['index']))
    
    sequence.sort(key=lambda x: x[1])
    
    return sequence