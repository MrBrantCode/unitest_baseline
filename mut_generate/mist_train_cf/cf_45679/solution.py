"""
QUESTION:
Create a function `process_2D_vector` that takes a 2D vector `m` as input, where `m` is a list of lists. The function should return a new 2D vector `m'` where each sub-vector at an index that is a multiple of 5 is sorted in ascending order, and all other sub-vectors remain unchanged.
"""

def process_2D_vector(m):
    return [sorted(sublist) if i % 5 == 0 else sublist for i, sublist in enumerate(m)]