"""
QUESTION:
Write a function `find_pairs(sequence, target_sum)` that takes in a list of integers `sequence` and an integer `target_sum`, and returns a list of tuples representing the unique pairs of integers in the sequence that sum up to the target sum, with the order of the pairs not mattering. The pairs should be ordered in a way that the smaller number comes first.
"""

def find_pairs(sequence, target_sum):
    pairs = set()
    seen = set()
    
    for num in sequence:
        complement = target_sum - num
        if complement in seen:
            pair = (min(num, complement), max(num, complement))
            pairs.add(pair)
        seen.add(num)
    
    return list(pairs)