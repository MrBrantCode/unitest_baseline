"""
QUESTION:
Write a function `find_pairs` that takes a list of integers as input and returns the first three pairs of consecutive integers with a difference of less than 4. If less than three pairs exist, return all pairs found. The function should consider edge cases and have an efficient time complexity.
"""

def find_pairs(lst):
    pairs = []
    for i in range(len(lst)-1):  
        if abs(lst[i] - lst[i+1]) < 4:
            pairs.append((lst[i], lst[i+1]))
            if len(pairs) == 3:
                break
    return pairs