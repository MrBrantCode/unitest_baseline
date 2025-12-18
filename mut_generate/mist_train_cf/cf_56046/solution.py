"""
QUESTION:
Write a function `merge_and_check(set1, set2)` that takes two sets `set1` and `set2` as input, merges them into a new set without duplicates, and checks if the length of the merged set is a perfect square. The function should return the merged set and a boolean indicating whether its size is a perfect square.
"""

def merge_and_check(set1, set2):
    # merge the two sets
    merged_set = set1.union(set2)
    
    # calculate the size of the merged set
    size = len(merged_set)
    
    # check if the size is a perfect square
    is_perfect_square = size**0.5 == int(size**0.5)
    
    return merged_set, is_perfect_square