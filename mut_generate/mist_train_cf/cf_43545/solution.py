"""
QUESTION:
Create a function `make_a_pile(n, pattern, offset=0)` that generates a list representing the number of stones in each level of a pile. The pile has `n` levels, and the number of stones in each level is determined by the `pattern` ('odd' or 'even') and the preceding level's stones. The first level starts with `n` stones plus an optional `offset`. For 'odd' pattern, add the next odd number to the previous level's stones, and for 'even' pattern, add the next even number to the previous level's stones. Return the list of stones in each level, where the element at index `i` represents the number of stones in level `(i+1)`.
"""

def make_a_pile(n, pattern, offset=0):
    stones = [n + offset]
    for i in range(n-1):
        if pattern == 'odd':
            stones.append(stones[-1] + 2*i + 1)
        elif pattern == 'even':
            stones.append(stones[-1] + 2*(i + 1))
    return stones