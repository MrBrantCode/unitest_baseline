"""
QUESTION:
The function `colorings` should calculate the total number of distinct valid colorings possible for a grid of 64 triangles. The triangles can be filled with one of three colors (1, 2, or 3) such that no pair of adjacent triangles share the same color. Two triangles are considered neighbors if they share a common edge. The function should consider all possible colorings, including rotations and reflections.
"""

from functools import lru_cache

@lru_cache(maxsize=None) 
def entrace(idx=0, top=0, left=0, bottom=0):
    if idx == 64: 
        return 1
    count = 0
    for c in [1, 2, 3]: 
        if c != top: 
            if idx % 8 > 0 and idx % 8 < 7: 
                if c != left:
                    count += 3*entrace(idx+1, c, c, bottom=1) + 3*entrace(idx+1, c, c, bottom=2)
                else: 
                    count += 2*entrace(idx+1, c, c, bottom=1)
            else: 
                if idx % 8 == 0: 
                    count += entrace(idx+1, c, 0, bottom=0)
                else: 
                    count += entrace(idx+1, 0, 0, bottom=0)  
    return count