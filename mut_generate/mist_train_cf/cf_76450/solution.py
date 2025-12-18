"""
QUESTION:
Write a function `make_a_pile(n, pattern)` that generates a list of the number of stones in each level of a pile of `n` levels, following the given `pattern` of 'odd' or 'even'. The first level starts with `n` stones, and each subsequent level adds the next odd or even number to the previous level's stones, depending on the `pattern`. The function should return a list where the element at index `i` represents the number of stones in level `(i+1)`.
"""

def make_a_pile(n, pattern):
    if pattern == 'odd':
        p = [1]
        stone = 1
        for i in range(n-1):
            stone += 2
            p.append(stone)
    elif pattern == 'even':
        p = [2]
        stone = 2
        for i in range(n-1):
            stone += 2
            p.append(stone)
    return p