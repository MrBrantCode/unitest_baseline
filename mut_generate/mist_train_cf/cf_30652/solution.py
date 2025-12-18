"""
QUESTION:
Implement a function `unique_values(pairs)` that takes a list of pairs as input, where each pair is a tuple with two elements, and returns a list of unique values from the pairs. The function should exclude duplicate values from the output list.
"""

def unique_values(pairs):
    unique_set = set()  
    for pair in pairs:
        unique_set.add(pair[1])  
    return list(unique_set)